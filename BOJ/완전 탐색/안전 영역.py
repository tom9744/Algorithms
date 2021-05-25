import sys
from collections import deque
input = sys.stdin.readline


def BFS(graph, thresh, src_x, src_y):
    queue = deque()
    queue.append((src_x, src_y))

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for n in range(4):
            nx, ny = x + dx[n], y + dy[n]

            if 0 <= nx < N and 0 <= ny < N:
                if thresh < graph[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


N = int(input())

heights = []
max_height = 0

for _ in range(N):
    temp = list(map(int, input().split()))
    heights.append(temp)

    max_height = max(max_height, max(temp))

max_count = 0

for height in range(max_height):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if height < heights[i][j] and not visited[i][j]:
                visited[i][j] = True
                BFS(heights, height, i, j)
                count += 1

    max_count = max(max_count, count)

print(max_count)
