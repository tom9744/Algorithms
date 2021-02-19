# 1707 : 이분 그래프
#
# 이분 그래프가 뭔지 몰라서 찾아봤더니, 거리가 1만큼 떨어진 노드의 색상이 모두 다른 그래프라고 한다.
# 따라서, BFS 탐색을 통해 같은 Level 상에 있는 노드는 같은 색으로 칠해준다.
# 칠해주다가, Level 단계 차이가 1단계 밖에 나지 않는데 색상이 같은 노드가 발견되면 이분 그래프가 아닌 것이다.
#
# 로직은 얼추 맞는거 같고 50%까지 채점이 진행되었는데, 계속 답이 틀렸다고 나와서 또 검색을 했더니
# 문제 자체에서 간과한 부분이 있었고, "그래프가 하나의 연결된 그래프가 주어지는 것이 아닐 수 있다"라는 점이었다.

from sys import stdin
from collections import deque


def BFS(start_node):
    queue = deque()
    queue.append(start_node)

    visited[start_node] = 1
    colored[start_node] = 1

    while queue:
        current = queue.popleft()

        for node in graph[current]:
            # 다음 노드가 현재 노드와 색상이 같다면, 이분 그래프 불가능
            if colored[current] == colored[node]:
                return False
            # 다음 노드가 현재 노드와 색상이 다르다면, 색칠한다.
            else:
                if colored[current] == 1:
                    colored[node] = 2
                else:
                    colored[node] = 1

            # 아직 방문하지 않은 노드인 경우
            if visited[node] == 0:
                visited[node] = 1
                queue.append(node)

    return True


K = int(stdin.readline().rstrip())

for _ in range(K):
    V, E = map(int, stdin.readline().rstrip().split())
    is_bipartite = True

    graph = [[] for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]
    colored = [0 for _ in range(V + 1)]

    for _ in range(E):
        nodeA, nodeB = map(int, stdin.readline().rstrip().split())

        graph[nodeA].append(nodeB)
        graph[nodeB].append(nodeA)

    for vertex in range(1, V + 1):
        if visited[vertex] == 0:
            if not BFS(vertex):
                is_bipartite = False

    if is_bipartite:
        print("YES")
    else:
        print("NO")
