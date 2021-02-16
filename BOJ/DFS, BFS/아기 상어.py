from sys import stdin
from collections import deque
import heapq

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(current_size, current_position):
    available_fish = []
    queue = deque()
    queue.append(current_position)
    moves[current_position[0]][current_position[1]] = 1

    while queue:
        x, y = queue.popleft()

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < N and 0 <= ny < N and moves[nx][ny] == 0:
                # 해당 위치에 물고기가 있는 경우
                if water[nx][ny] > 0:
                    fish_size = water[nx][ny]
                    # 물고기 크기가 상어보다 작은 경우
                    if fish_size < current_size:
                        heapq.heappush(available_fish, [moves[x][y], nx, ny])
                    # 물고기 크기가 상어보다 큰 경우
                    elif fish_size > current_size:
                        continue

                moves[nx][ny] = moves[x][y] + 1
                queue.append([nx, ny])

    return available_fish


N = int(stdin.readline().rstrip())
water = []
shark_position = [0, 0]
shark_size = 2
eaten = 0
survived = 0

for row in range(N):
    line = list(map(int, stdin.readline().rstrip().split()))
    for col in range(N):
        if line[col] == 9:
            shark_position = [row, col]
    water.append(line)

while True:
    moves = [[0 for _ in range(N)] for _ in range(N)]
    target_fishes = BFS(shark_size, shark_position)
    nearest_fishes = []

    if not target_fishes:
        break

    min_distance = target_fishes[0][0]

    for fish in target_fishes:
        if fish[0] == min_distance:
            heapq.heappush(nearest_fishes, [fish[1], fish[2]])
        else:
            break

    # 가까운 물고기 중, 가장 위쪽과 왼쪽에 있는 물고기를 먹는다.
    if nearest_fishes:
        eaten_fish = heapq.heappop(nearest_fishes)

        water[shark_position[0]][shark_position[1]] = 0  # 상어 빈자리
        water[eaten_fish[0]][eaten_fish[1]] = 9          # 상어가 먹은 물고기 자리

        shark_position = eaten_fish

        eaten += 1
        survived += min_distance

        if eaten == shark_size:
            shark_size += 1
            eaten = 0

print(survived)
