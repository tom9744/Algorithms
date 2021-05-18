from collections import deque


def solution(maps):
    def BFS(height, width):
        queue = deque()
        queue.append((0, 0))
        maps[0][0] = -1

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while queue:
            x, y = queue.popleft()

            for n in range(4):
                nx = x + dx[n]
                ny = y + dy[n]

                if 0 <= nx < height and 0 <= ny < width:
                    if maps[nx][ny] == 1:
                        maps[nx][ny] = maps[x][y] - 1
                        queue.append((nx, ny))

    BFS(len(maps), len(maps[0]))

    if maps[-1][-1] != 1:
        return -maps[-1][-1]
    else:
        return -1