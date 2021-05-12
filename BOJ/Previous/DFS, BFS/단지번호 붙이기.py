# 동 서 남 북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def DFS(map, x, y):
    visited = list()
    stack = [[x, y], ]

    map[x][y] = -1  # 해당 위치 방문 처리
    count = 1  # 단지를 구성하는 집의 개수

    while len(stack) != 0:
        current = stack.pop()

        if current not in visited:
            visited.append(current)

            for direction in range(4):
                next_x = current[0] + dx[direction]
                next_y = current[1] + dy[direction]
                length = len(map)

                # 지도 범위 내에 존재하는 묶음처리 되지 않은 집을 Stack 에 추가한다.
                next_checks = []
                if 0 <= next_x < length and 0 <= next_y < length and map[next_x][next_y] == 1:
                    next_checks.append([next_x, next_y])
                    map[next_x][next_y] = -1  # 방문 처리
                    count += 1  # 단지를 구성하는 집 개수 1개 추가
                stack.extend(next_checks)

    return count


N = int(input())
houses = []  # 집 위치 정보를 저장하기 위한 배열
complexes = []  # 단지를 구성하는 집의 개수를 저장하기 위한 배열

for _ in range(N):
    row = list(map(int, list(input())))
    houses.append(row)

for x in range(N):
    for y in range(N):
        # 아직 하나의 단지로 묶음처리 되지 않은 집이 있는 경우, DFS 수행
        if houses[x][y] == 1:
            complexes.append(DFS(houses, x, y))

complexes.sort()

# 정답 출력
print(len(complexes))

for each in complexes:
    print(each)

