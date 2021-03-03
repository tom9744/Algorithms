# 11048 : 이동하기
#
# 문제에서 주어진 대로 미로를 탐색하면서 DP[x][y] = max(DP[x][y], maze[x][y] + DP[px][py])를 수행한다.

N, M = map(int, input().split())
DP = [[0 for _ in range(M)] for _ in range(N)]
maze = []

for _ in range(N):
    maze.append(list(map(int, input().split())))

DP[0][0] = maze[0][0]

dx = [1, 0, 1]
dy = [0, 1, 1]

for row in range(N):
    for col in range(M):
        x, y = row, col

        for direction in range(3):
            px = x - dx[direction]
            py = y - dy[direction]

            if 0 <= px < N and 0 <= py < M:
                DP[x][y] = max(DP[x][y], maze[x][y] + DP[px][py])

print(DP[N - 1][M - 1])