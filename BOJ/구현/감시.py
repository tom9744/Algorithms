import sys
input = sys.stdin.readline


# 각 CCTV 마다 바라볼 수 있는 방향의 모든 조합을 구한다.
def get_combination(path, index):
    if len(path) == len(cameras):
        return [path[:]]

    result = []
    _, _, camera = cameras[index]
    possible_directions = directions[camera]

    for direct in possible_directions:
        result.extend(get_combination(path + [direct], index + 1))

    return result


# 한 방향으로 바라 보았을 때, 벽에 가라지 않고 커버할 수 있는 범위를 반환한다.
def calc_range(src_x, src_y, direct):
    count = 0
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    nx = src_x + dx[direct]
    ny = src_y + dy[direct]

    while 0 <= nx < N and 0 <= ny < M:
        if office[nx][ny] == 6:
            break
        # CCTV, 벽이 아닌 공간이며, 방문한 적 없는 경우
        if office[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            count += 1

        nx += dx[direct]
        ny += dy[direct]

    return count


N, M = map(int, input().split())

directions = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],
    5: [[0, 1, 2, 3]]
}

office = []
cameras = []
area = 0

# 사무실 지형과 CCTV 배치 정보를 입력 받는다.
for i in range(N):
    line = list(map(int, input().split()))

    # CCTV 위치 정보와 종류를 기록한다.
    for j, cell in enumerate(line):
        if cell == 0:
            area += 1
        elif cell < 6:
            cameras.append((i, j, cell))

    office.append(line)

# 각 CCTV 마다 바라볼 수 있는 방향으로 만들 수 있는 모든 조합을 구한다.
combinations = get_combination([], 0)
max_covered_area = 0

# 조합의 각 요소에 대해, 커버할 수 있는 전체 넓이를 구해본다.
for combination in combinations:
    visited = [[False] * M for _ in range(N)]
    covered_area = 0

    # 각 카메라가 커버할 수 있는 넓이를 구한다.
    for cam_num, direction in enumerate(combination):
        x, y, _ = cameras[cam_num]
        individual_count = 0

        for direct in direction:
            individual_count += calc_range(x, y, direct)

        covered_area += individual_count  # 한 카메라가 커버하는 범위를 전체에 합산한다.

    # 최대값을 구한다.
    max_covered_area = max(max_covered_area, covered_area)

print(area - max_covered_area)
