# 14499: 주사위 굴리기

from sys import stdin

N, M, x, y, K = map(int, stdin.readline().rstrip().split())
field = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
moves = list(map(int, stdin.readline().rstrip().split()))

# 1: 동, 2: 서, 3:남, 4:북
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

position = (x, y)
status = [0, 0, 0, 0, 0, 0]  # 위, 북, 동, 남, 서, 바닥

for move in moves:
    nx, ny = position[0] + dx[move], position[1] + dy[move]

    if 0 <= nx < N and 0 <= ny < M:
        if move == 1:
            status[0], status[2], status[4], status[5] = status[4], status[0], status[5], status[2]
        if move == 2:
            status[0], status[2], status[4], status[5] = status[2], status[5], status[0], status[4]
        if move == 3:
            status[0], status[1], status[3], status[5] = status[3], status[0], status[5], status[1]
        if move == 4:
            status[0], status[1], status[3], status[5] = status[1], status[5], status[0], status[3]

        if field[nx][ny] == 0:
            field[nx][ny] = status[5]
        else:
            status[5] = field[nx][ny]
            field[nx][ny] = 0

        position = (nx, ny)

        print(status[0])
