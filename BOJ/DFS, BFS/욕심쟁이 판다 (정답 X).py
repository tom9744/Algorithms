# 1937 : 욕심쟁이 판다
#
# 백 트래킹으로 접근했는데 시간초과에 걸렸다.
# 문제 분류를 확인해보니 DP 문제여서 나중에 다시 풀어야겠다.

from sys import stdin

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(start, days_passed):
    global maximum_day
    maximum_day = max(maximum_day, days_passed)

    stack = list()
    stack.append(start)

    while stack:
        x, y = stack.pop(0)

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < N and 0 <= ny < N and forest[x][y] < forest[nx][ny]:
                visited[nx][ny] = 1
                DFS([nx, ny], days_passed + 1)
                visited[nx][ny] = 0


N = int(stdin.readline().rstrip())
visited = [[0 for _ in range(N)] for _ in range(N)]
forest = []
maximum_day = 0

for _ in range(N):
    forest.append(list(map(int, stdin.readline().rstrip().split())))

for row in range(N):
    for col in range(N):
        DFS([row, col], 1)

print(maximum_day)