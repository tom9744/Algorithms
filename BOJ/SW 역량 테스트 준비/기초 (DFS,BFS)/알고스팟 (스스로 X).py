# 1261: 알고스팟
#
# 비용이 0일 때, appendleft()로 Queue의 최상단에 넣어줌으로써
# 최소 비용 거리를 구할 수 있다.

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(graph, node):
    queue = deque()
    queue.append(node)

    startX, startY = node
    visited[startX][startY] = 0

    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if maze[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx, ny))
                elif maze[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


M, N = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

BFS(maze, (0, 0))

print(visited[N - 1][M - 1])
