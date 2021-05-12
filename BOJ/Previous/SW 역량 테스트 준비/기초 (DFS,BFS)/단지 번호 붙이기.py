# 2667: 단지 번호 붙이기

from collections import deque

N = int(input())
apartComplex = [list(map(int, input())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
numOfComplex = 0
counts = []


def BFS(graph, node, count):
    queue = deque()
    queue.append(node)

    while queue:
        curr = queue.popleft()

        for idx in range(4):
            nx = curr[0] + dx[idx]
            ny = curr[1] + dy[idx]

            # 범위 내에 있으며 아직 방문하지 않은 아파트 단지
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = -1
                queue.append((nx, ny))
                count += 1

    return count


for row in range(N):
    for col in range(N):
        if apartComplex[row][col] == 1:
            apartComplex[row][col] = -1  # 방문 처리
            counts.append(BFS(apartComplex, (row, col), 1))  # BFS 탐색 수행
            numOfComplex += 1  # 단지 수 증가

print(numOfComplex)  # 단지 개수 출력

for cnt in sorted(counts):  # 단지 속하는 집의 수 오름차순으로 출력
    print(cnt)
