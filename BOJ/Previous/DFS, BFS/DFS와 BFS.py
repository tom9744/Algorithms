# 1260 : DFS와 BFS
#
# 양방향 그래프는 adj[][] 과 같은 2차원 배열로 그리는 것이 오류 발생 가능성이 낮다.
#
# 작은 수부터 방문한다고 하였으므로, DFS 의 경우 자식 노드를 내림차순/ BFS 의 경우 자식 노드를 오름차순하여
# 각각 Stack 과 Queue 에 추가하면 된다.


def DFS(graph, start_vertex):
    visited = list()
    stack = list()

    stack.append(start_vertex)

    while len(stack) != 0:
        current = stack.pop()

        if current not in visited:
            visited.append(current)
            children = []
            for idx in range(len(graph[current])):
                if graph[current][idx] == 1:
                    children.append(idx)

            stack.extend(sorted(children, reverse=True))

    return visited


def BFS(graph, start_vertex):
    visited = list()
    queue = list()

    queue.append(start_vertex)

    while len(queue) != 0:
        current = queue.pop(0)

        if current not in visited:
            visited.append(current)
            children = []
            for idx in range(len(graph[current])):
                if graph[current][idx] == 1:
                    children.append(idx)

            queue.extend(sorted(children))

    return visited


N, M, V = map(int, input().split())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 그래프를 작성한다.
for _ in range(M):
    vertexA, vertexB = map(int, input().split())

    graph[vertexA][vertexB] = graph[vertexB][vertexA] = 1

for each in DFS(graph, V):
    print(each, end=" ")

print()

for each in BFS(graph, V):
    print(each, end=" ")
