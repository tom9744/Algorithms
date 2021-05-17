from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    queue = deque()
    queue.append((0, 0))    # 시작점 (0, 0)을 큐에 추가한다.
    maze[0][0] = -1         # 시작점 (0, 0)에 경과시간을 음수로 저장하여, 방문표시한다.

    while queue:
        x, y = queue.popleft()

        # 상하좌우 네 방향의 노드를 방문한다.
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]

            if 0 <= nx < N and 0 <= ny < M:
                # 아직 방문하지 않은 경우, 경과 시간을 표시함으로써 방문 표시하고, 큐에 추가한다.
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] - 1
                    queue.append((nx, ny))


bfs()

print(-maze[N - 1][M - 1])

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# result: 10
