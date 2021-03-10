# 13023: ABCDE
#
# 시작부터 문제가 제대로 이해되지 않아서 고생한 문제였다.
#
# 항상 끝까지 한번만 탐색하면 DFS/BFS 문제만 접했는데, 이번 문제는
# 한 정점에서 시작해 그래프를 탐색하는 모든 경우의 수에 대해 도달할 수 있는 최대 깊이를 구해야 했다.
#
# 위와 같은 로직을 구현하기 위해 방문 후에 다시 visited 배열의 값을 False 상태로 원상복구한다.
#
# 또한, 답을 찾은 경우(depth >= 4) 더 이상 탐색을 수행하지 않도록 하여야
# 시간초과에 걸리지 않고 문제를 풀이할 수 있다.


from sys import stdin


def DFS(graph, node, visited, depth):
    global possible
    visited[node] = True

    # 깊이가 4 이상인 경우 답을 찾은 것이다.
    if depth >= 4:
        possible = True
        return  # 답을 찾은 경우, 탐색을 종료해야 한다.

    for adjacentNode in graph[node]:
        if not visited[adjacentNode]:
            DFS(graph, adjacentNode, visited, depth + 1)
            visited[adjacentNode] = False  # 전체 탐색을 위해 다시 False 설정.


N, M = map(int, stdin.readline().rstrip().split())
relations = [[] for _ in range(N)]
visited = [False for _ in range(N)]
possible = False

for _ in range(M):
    personA, personB = map(int, stdin.readline().rstrip().split())
    relations[personA].append(personB)
    relations[personB].append(personA)

for person in range(N):
    DFS(relations, person, visited, 0)
    visited[person] = False  # 마찬가지로 다음 반복을 위해 visited 배열 원상복구.

    if possible:
        break

if possible:
    print(1)
else:
    print(0)
