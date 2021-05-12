# 1967 : 트리의 지름
#
# 100% 까지 채점이 진행되는데 100%에서 틀렸다고 나온다.
# 검색을 해봐도 정답 코드랑 내 코드가 다른게 없는데 뭐가 문젠지 모르겠다.

from sys import stdin
from collections import deque


def BFS(start, mode):
    queue = deque()
    queue.append(start)

    visited = [-1 for _ in range(N + 1)]
    visited[start] = 0

    while queue:
        current = queue.popleft()

        for child_node, distance in graph[current]:
            if visited[child_node] == -1:
                visited[child_node] = visited[current] + distance
                queue.append(child_node)

    max_distance = max(visited)

    if mode == 1:
        return visited.index(max_distance)
    else:
        return max_distance


N = int(stdin.readline().rstrip())
graph = [[] for _ in range(N)]

for _ in range(N - 1):
    parent, child, weight = list(map(int, stdin.readline().rstrip().split()))

    graph[parent - 1].append([child - 1, weight])
    graph[child - 1].append([parent - 1, weight])

radius = BFS(BFS(0, 1), 2)

print(radius)

