import sys

from collections import deque

input = sys.stdin.readline


# 조합을 생성하는 DFS 함수
def DFS(coordinates, count, path, index=0):
    if count == 0:
        return [path[:]]

    result = []

    for idx in range(index, len(coordinates)):
        path.append(coordinates[idx])
        result.extend(DFS(coordinates, count - 1, path, idx + 1))
        path.pop()

    return result


# 바이러스가 전파되는 셀의 개수를 세는 BFS 함수
def BFS(graph, src_x, src_y):
    queue = deque()

    visited[src_x][src_y] = True
    queue.append((src_x, src_y))

    count = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for n in range(4):
            nx, ny = x + dx[n], y + dy[n]

            # 범위 내의 빈 방이며, 아직 방문하지 않은 경우만 큐에 삽입한다.
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == "0":
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

                    count += 1

    return count


N, M = map(int, input().split())
graph, aisles, walls, viruses = [], [], [], []

# 연구소 지형을 입력 받는다.
for i in range(N):
    cells = input().split()

    # 각 지형에 해당하는 좌표값을 배열에 저장한다.
    for j, cell in enumerate(cells):
        if cell == "1":
            walls.append((i, j))
        elif cell == "2":
            viruses.append((i, j))
        else:
            aisles.append((i, j))

    graph.append(cells)

# 빈 방에 해당하는 좌표 3개를 선택하는 조합을 만든다.
candidates = DFS(aisles, 3, [])
min_infected = float("inf")

# 모든 조합에 대해 벽을 세우고, 바이러스를 퍼뜨려본다.
for candidate in candidates:
    for x, y in candidate:
        graph[x][y] = "1"

    visited = [[False] * M for _ in range(N)]
    total = 0

    # 모든 바이러스 좌표에 대해, 전파를 시작한다.
    for virus in viruses:
        total += BFS(graph, virus[0], virus[1])

    min_infected = min(min_infected, total)  # 가장 적게 전파된 경우를 저장한다.

    # 벽을 세웠던 위치를 빈 방으로 초기화해준다.
    for x, y in candidate:
        graph[x][y] = "0"

# 안전지대의 개수 = 전체 셀 개수 - 감염된 셀 개수 - (벽의 개수 + 3)
print(N * M - min_infected - len(walls) - 3)
