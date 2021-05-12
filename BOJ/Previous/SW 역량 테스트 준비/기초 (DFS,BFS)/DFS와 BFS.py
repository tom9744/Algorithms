# 1260: DFS와 BFS
#
# DFS 구현 시 Stack 자료구조를, BFS 구현 시 Queue(Deque) 자료구조를 사용한다.

from collections import deque


def DFS(graph, node, visited):
    visited[node] = True

    print(node, end=" ")

    for adjacentNode in sorted(graph[node]):
        if not visited[adjacentNode]:
            DFS(graph, adjacentNode, visited)


def BFS(graph, node, visited):
    queue = deque()
    queue.append(node)
    visited[node] = True

    while queue:
        current = queue.popleft()

        print(current, end=" ")

        for adjacentNode in sorted(graph[current]):
            if not visited[adjacentNode]:
                queue.append(adjacentNode)
                visited[adjacentNode] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    nodeA, nodeB = map(int, input().split())

    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)

visited = [False for _ in range(N + 1)]
visited[0] = True
DFS(graph, V, visited)

print()

visited = [False for _ in range(N + 1)]
visited[0] = True
BFS(graph, V, visited)
