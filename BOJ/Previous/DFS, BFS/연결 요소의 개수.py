# 11724 : 연결 요소의 개수
#
# 보통의 경우 visited 배열을 DFS 내부에 선언하여 사용하는데, 이번 문제의 경우는
# 함수 외부에 각 노드에 대한 방문 여부를 저장하는 배열을 선언하여 사용해야 한다.
#
# 각 노드에 대해 반복문을 수행하며 방문 여부를 따지고, 방문하지 않은 경우에만 DFS 를 수행해 연결된 노드를 방문처리 한다.
#
# DFS 가 호출된 횟수가 연결 요소의 개수이다.

import sys


def DFS(visited, graph, node):
    stack = [node, ]

    while len(stack) != 0:
        current = stack.pop()

        if visited[current] is False:
            visited[current] = True

            next_nodes = []
            for index in range(len(graph[current])):
                if graph[current][index] == 1:
                    next_nodes.append(index)

            stack.extend(next_nodes)


N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
is_visited = [False for _ in range(N + 1)]
count = 0

for _ in range(M):
    vertexA, vertexB = map(int, sys.stdin.readline().rstrip().split())
    graph[vertexA][vertexB] = 1
    graph[vertexB][vertexA] = 1

for node in range(1, N + 1):
    if is_visited[node] is False:
        DFS(is_visited, graph, node)
        count += 1

print(count)