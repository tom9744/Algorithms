# 11724: 연결 요소의 개수
#
# 전체 노드를 처음부터 끝까지 순회하면서 DFS 탐색을 수행하는데,
# 이미 한 번 방문한 노드는 방문처리를 해놓는다.
#
# 방문 처리된 노드에 대해서는 DFS 탐색을 수행하지 않고,
# DFS 탐색이 수행된 횟수를 누적하면 정답이다.


def DFS(graph, startNode, visited):
    visited[startNode] = True

    for adjacentNode in graph[startNode]:
        if not visited[adjacentNode]:
            DFS(graph, adjacentNode, visited)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
visited[0] = True

for _ in range(M):
    nodeA, nodeB = map(int, input().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)

count = 0

for node in range(1, N + 1):
    if not visited[node]:
        DFS(graph, node, visited)
        count += 1

print(count)
