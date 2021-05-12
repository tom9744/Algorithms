# 2206 : 벽 부수고 이동하기
#
# 연구소 문제처럼 벽을 부술 수 있는 모든 경우에 대해 BFS 수행하니 시간 초과가 걸린다.
# 검색해보니 3차원 배열을 이용해 BFS 탐색을 단 한번만 수행하면서 풀 수 있는 방법을 찾게 되었다.
#
# tracker[x][y][z]가 있을 때, tracker[x][y][1]는 (x, y) 위치에서 아직 벽을 부수지 않은 상태를 나타내고,
# tracker[x][y][0]는 (x, y) 위치에서 벽을 이미 부순 상태를 나타내도록 한다.
# 쉽게 말해 'z'의 값이 벽을 부술 수 있는 남은 횟수라고 생각하면 된다.
#
# 따라서 (0, 0, 1)부터 시작하며, 벽이 아니고(field[nx][ny] == 0) 방문한 적 없는(tracker[nx][ny][z] == 0) 경우는
# 일반적인 BFS 탐색을 수행해 최단 거리를 찾는 방법처럼 Queue 에 추가한다.
#
# 벽이고(field[nx][ny] == 1) 아직 벽을 한번도 부수지 않은 경우(z == 1)에는
# tracker[nx][ny][0] = tracker[x][y][z] + 1 와 같이 'z'의 값을 0으로 바꾸어준다.
#
# Queue 에서 꺼낸 x, y 값이 N - 1, M - 1이라면 tracker[x][y][z]을,
# N - 1, M - 1에 도달하지 못하고 반복문이 종료되면 -1을 반환한다.

from sys import stdin
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS():
    queue = deque()
    queue.append((0, 0, 1))
    tracker[0][0][1] = 1

    while queue:
        x, y, z = queue.popleft()

        if x == N - 1 and y == M - 1:
            return tracker[x][y][z]

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < N and 0 <= ny < M:
                if field[nx][ny] == 0 and tracker[nx][ny][z] == 0:
                    tracker[nx][ny][z] = tracker[x][y][z] + 1
                    queue.append((nx, ny, z))
                elif field[nx][ny] == 1 and z == 1:
                    tracker[nx][ny][0] = tracker[x][y][z] + 1
                    queue.append((nx, ny, 0))

    return -1


N, M = map(int, stdin.readline().rstrip().split())
field = []
tracker = [[[0] * 2 for _ in range(M)] for _ in range(N)]
for row in range(N):
    field.append(list(map(int, list(stdin.readline().rstrip()))))

print(BFS())

# from sys import stdin
# from collections import deque
# from copy import deepcopy
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
#
# def BFS():
#     queue = deque()
#     queue.append((0, 0))
#     field_copy[0][0] = 1
#
#     while queue:
#         x, y = queue.popleft()
#
#         for direction in range(4):
#             nx = x + dx[direction]
#             ny = y + dy[direction]
#
#             if 0 <= nx < N and 0 <= ny < M and field_copy[nx][ny] == 0:
#                 field_copy[nx][ny] = field_copy[x][y] + 1
#                 queue.append((nx, ny))
#
#
# N, M = map(int, stdin.readline().rstrip().split())
# field = []
# walls = []
# for row in range(N):
#     line = list(map(int, list(stdin.readline().rstrip())))
#     for col in range(M):
#         if line[col] == 1:
#             walls.append((row, col))
#     field.append(line)
#
# min_move = 100000000
# answer_exist = False
#
# for r, c in walls:
#     field_copy = deepcopy(field)
#     field_copy[r][c] = 0
#
#     BFS()
#
#     if field_copy[N - 1][M - 1] != 0:
#         if field_copy[N - 1][M - 1] < min_move:
#             min_move = field_copy[N - 1][M - 1]
#             answer_exist = True
#
# if answer_exist:
#     print(min_move)
# else:
#     print(-1)


