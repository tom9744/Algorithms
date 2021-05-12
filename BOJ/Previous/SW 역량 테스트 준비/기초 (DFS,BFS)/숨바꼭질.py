# 1697: 숨바꼭질
#
# 직선 위의 하나의 점에서 1초 후 도달할 수 있는 위치로 구성된 그래프를 작성한다.
#
# 이후 BFS 탐색을 통해 원하는 지점까지의 최단거리를 구하면 된다.

from collections import deque


def BFS(graph, node, targetNode):
    queue = deque()
    queue.append(node)
    visited[node] = 0

    while queue:
        curr = queue.popleft()

        if curr == targetNode:
            return

        # 도달할 수 있는 위치 중에서
        for adjNode in graph[curr]:
            # 범위 내에 있으며, 방문하지 않은 것에 대해
            if 0 <= adjNode <= 100000 and visited[adjNode] == -1:
                # 방문 처리를 하고 경과 시간을 누적한다
                visited[adjNode] = visited[curr] + 1
                queue.append(adjNode)


line = [[i - 1, i + 1, i * 2] for i in range(100001)]  # 각 위치에서 도달할 수 있는 위치
visited = [-1 for _ in range(100001)]  # 방문 처리를 위한 배열

N, K = map(int, input().split())

BFS(line, N, K)

print(visited[K])  # 도착한 위치를 방문한 순서 (= 깊이) 출력
