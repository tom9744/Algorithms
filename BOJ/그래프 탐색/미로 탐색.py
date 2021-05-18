import collections

N, M = map(int, input().split())
maze_array = [list(map(int, input())) for _ in range(N)]


def BFS(src_x, src_y):
    queue = collections.deque()
    queue.append((src_x, src_y))
    maze_array[src_x][src_y] = -1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]

            if 0 <= nx < N and 0 <= ny < M:
                if maze_array[nx][ny] == 1:
                    maze_array[nx][ny] = maze_array[x][y] - 1
                    queue.append((nx, ny))


BFS(0, 0)
print(-maze_array[-1][-1])
