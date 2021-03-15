from collections import deque
from sys import stdin


def BFS(graph, node):
    queue = deque()
    queue.append(node)
    checked[node] = 0

    while queue:
        curr = queue.popleft()

        for adjNode in graph[curr]:
            if checked[adjNode] == -1:
                if checked[curr] == 0:
                    checked[adjNode] = 1
                elif checked[curr] == 1:
                    checked[adjNode] = 0
                queue.append(adjNode)

            else:
                if checked[curr] == checked[adjNode]:
                    return False
    return True


K = int(input())

for _ in range(K):

    V, E = map(int, stdin.readline().rstrip().split())
    graph = [[] for _ in range(V + 1)]
    checked = [-1 for _ in range(V + 1)]
    checked[0] = -100
    isBipartite = True

    for _ in range(E):
        verA, verB = map(int, stdin.readline().rstrip().split())
        graph[verA].append(verB)
        graph[verB].append(verA)

    for vertex in range(1, V + 1):
        if checked[vertex] == -1:
            if not BFS(graph, vertex):
                isBipartite = False
                break

    print("YES" if isBipartite else "NO")
