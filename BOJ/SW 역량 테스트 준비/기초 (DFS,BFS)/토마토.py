# 7576: 토마토

from collections import deque
from sys import stdin

M, N = map(int, stdin.readline().rstrip().split())
box = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ripeTomatoes = []
emptyCount = 0
dayCount = 0

for row in range(N):
    for col in range(M):
        if box[row][col] == 1:
            ripeTomatoes.append((row, col))
        elif box[row][col] == -1:
            emptyCount += 1


def BFS(graph, nodes):
    global dayCount
    count = len(nodes)
    queue = deque(nodes)

    while queue:
        curr = queue.popleft()

        for idx in range(4):
            nx = curr[0] + dx[idx]
            ny = curr[1] + dy[idx]

            # 범위 내에 있으며, 아직 익지 않은 토마토
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[curr[0]][curr[1]] + 1  # BFS 탐색 마다 일수 증가
                dayCount = max(dayCount, graph[nx][ny])  # 지난 일수 최대값
                queue.append((nx, ny))
                count += 1  # 익힌 토마토 개수 증가

    return count


tomatoCount = BFS(box, ripeTomatoes)

# 익힌 토마토 개수가 (전체 - 빈칸) 개수와 같은 경우 모두 익힌 것이다
if tomatoCount == (N * M - emptyCount):
    print(dayCount - 1 if dayCount != 0 else 0)  # 일수가 0이면 토마토가 처음부터 다 익은 것
else:
    print(-1)
