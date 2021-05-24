import sys

from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    seq = list(map(int, input().split()))[1:]

    # 맨 첫번째 값은 '담당한 가수의 수'이므로 제외한다.
    for idx, num in enumerate(seq[:-1]):
        graph[num].append(seq[idx + 1])
        in_degree[seq[idx + 1]] += 1

# 위상정렬 수행
topological_sorted = []
queue = deque()

for idx in range(1, N + 1):
    if in_degree[idx] == 0:
        queue.append(idx)

while queue:
    now = queue.popleft()
    topological_sorted.append(now)

    for node in graph[now]:
        in_degree[node] -= 1

        if in_degree[node] == 0:
            queue.append(node)

# 위상정렬 결과가 노드의 개수보다 모자르면, 사이클이 발생한 것이다.
if len(topological_sorted) < N:
    print(0)
else:
    for node in topological_sorted:
        print(node)
