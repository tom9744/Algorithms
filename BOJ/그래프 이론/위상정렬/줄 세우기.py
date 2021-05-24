import sys

from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
in_degree = [0 for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())

    # 학생 A가 학생 B 앞에 서야한다.
    graph[A].append(B)
    in_degree[B] += 1  # 노드 B의 진입차수 1 증가

topology_sorted = []
queue = deque()

# 진입차수가 0인 노드를 모두 큐에 삽입한다.
for idx in range(1, N + 1):
    if in_degree[idx] == 0:
        queue.append(idx)

# 큐에서 노드를 하나씩 꺼내고, 결과 배열에 추가한다.
while queue:
    now = queue.popleft()
    topology_sorted.append(str(now))

    # 현재 노드와 연결된 노드들의 진입차수를 1 감소시킨다.
    for node in graph[now]:
        in_degree[node] -= 1

        # 만약 진입차수가 0이 되면, 큐에 삽입한다.
        if in_degree[node] == 0:
            queue.append(node)

print(" ".join(topology_sorted))
