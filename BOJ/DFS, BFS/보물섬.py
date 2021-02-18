# 2589 : 보물섬
#
# 지도 상의 모든 'L' 지점에 대해 BFS 탐색을 수행하여 시작점부터 육지 끝까지의 최단거리를 구한다.
# 이렇게 구한 최단거리들 중, 최대 값을 반환하면 정답이다.

from collections import deque
from sys import stdin

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(start):
    queue = deque()
    queue.append(start)

    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[start[0]][start[1]] = 1

    distance = 0

    while queue:
        x, y = queue.popleft()

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and landscape[nx][ny] == 'L':
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                distance = visited[x][y]

    return distance


N, M = map(int, stdin.readline().rstrip().split())
landscape = []
result = 0

for _ in range(N):
    landscape.append(list(stdin.readline().rstrip()))

for row in range(N):
    for col in range(M):
        if landscape[row][col] == 'L':
            shortest_distance = BFS([row, col])

            if result < shortest_distance:
                result = shortest_distance

print(result)