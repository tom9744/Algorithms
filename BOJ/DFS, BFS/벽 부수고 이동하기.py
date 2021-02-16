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


