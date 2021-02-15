# 16234 : 인구 이동
#
# 전체적인 로직은 올바르게 생각해 BFS 탐색으로 접근했는데, 문제를 살짝 잘못 이해해서 오답이 나왔다.
# 기존 코드는 아래에 주석처리 하여 보관해 놓았다.
#
# 기본적인 골자는 BFS 탐색을 통해 섬의 개수를 구하는 것과 동일하다. 배열의 모든 원소를 방문하면서
# 방문한 적이 있는 곳인지를 검토하고, 방문한 적이 없는 경우 BFS 탐색을 통해 하나의 그룹으로 묶는다.
#
# 이때 BFS 탐색을 수행하면서 구획의 총 인구수와 구획에 속하는 원소들의 좌표를 배열에 담는다.
# 탐색이 종료될 때, 반환된 좌표 배열의 길이가 1보다 크다면 연합을 구성한 것이므로 (총 인구수 // 구성 국가 수)로 인구 이동을 수행한다.
#
# 인구이동 수행 결과를 nations 배열에 반영한 뒤, 다시 BFS 탐색을 수행한다.
# 더 이상 인구를 이동할 수 없는 경우 (= 연합을 구성할 수 없는 경우) 종료하고 count 를 출력한다.

from sys import stdin
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(r, c):
    queue = deque()
    queue.append((r, c))

    united = [(r, c), ]
    population = nations[r][c]

    while queue:
        current = queue.popleft()

        for direction in range(4):
            nx = current[0] + dx[direction]
            ny = current[1] + dy[direction]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(nations[current[0]][current[1]] - nations[nx][ny]) <= R:
                    population += nations[nx][ny]
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    united.append((nx, ny))

    return united, population


N, L, R = map(int, stdin.readline().rstrip().split())
nations = []
count = 0

for _ in range(N):
    line = list(map(int, stdin.readline().rstrip().split()))
    nations.append(line)

while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    isDone = True
    new_population = 0

    for row in range(N):
        for col in range(N):
            if visited[row][col] == 0:
                visited[row][col] = 1
                united_nations, total_population = BFS(row, col)

                if len(united_nations) > 1:
                    new_population = total_population // len(united_nations)

                    for r, c in united_nations:
                        nations[r][c] = new_population

                    isDone = False

    if isDone:
        break

    count += 1

print(count)


# from sys import stdin
# from collections import deque
#
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
#
# def BFS(r, c, count):
#     queue = deque()
#     queue.append((r, c))
#
#     united = [(r, c), ]
#     population = nations[r][c]
#     visited[r][c] = count
#
#     while queue:
#         current = queue.popleft()
#
#         available = []
#         for direction in range(4):
#             nx = current[0] + dx[direction]
#             ny = current[1] + dy[direction]
#
#             if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
#                 if L <= abs(nations[current[0]][current[1]] - nations[nx][ny]) <= R:
#                     population += nations[nx][ny]
#                     visited[nx][ny] = count
#                     available.append((nx, ny))
#                     united.append((nx, ny))
#         queue.extend(available)
#
#     return united, population
#
#
# N, L, R = map(int, stdin.readline().rstrip().split())
# nations = []
# count = 0
#
# for _ in range(N):
#     line = list(map(int, stdin.readline().rstrip().split()))
#     nations.append(line)
#
# while True:
#     visited = [[0 for _ in range(N)] for _ in range(N)]
#     united_nations = []
#     union_counter = 1
#     new_population = 0
#
#     for row in range(N):
#         for col in range(N):
#             if visited[row][col] == 0:
#                 nation_list, total_population = BFS(row, col, union_counter)
#
#                 if len(nation_list) > 1:
#                     united_nations.append(nation_list)
#                     new_population = total_population // len(nation_list)
#                     union_counter += 1
#
#     if len(united_nations) == 0:
#         break
#     else:
#         for union in united_nations:
#             for r, c in union:
#                 nations[r][c] = new_population
#
#     count += 1
#
# print(count)
