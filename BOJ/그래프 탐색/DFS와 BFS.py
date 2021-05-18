import collections

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    src, dst = map(int, input().split())
    graph[src].append(dst)
    graph[dst].append(src)

# 각 간선 정보를 정렬하여, 낮은 수부터 방문할 수 있도록 한다.
for edge in graph:
    edge.sort()


def BFS(start):
    queue = collections.deque()
    queue.append(start)
    visited[start] = True

    while queue:
        now = queue.popleft()

        print(now, end=" ")

        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)


def DFS(start, visited=[]):
    print(start, end=" ")

    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            DFS(node, visited)


DFS(V)
print()
BFS(V)
