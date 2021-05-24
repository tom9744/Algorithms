# 우선순위 큐를 사용한 위상정렬
import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
in_deg = [0 for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_deg[B] += 1

queue = []
topological_sorted = []

# 일반 큐 대신, 우선순위 큐에 진입차수가 0인 문제번호를 삽입한다.
for num in range(1, N + 1):
    if in_deg[num] == 0:
        heapq.heappush(queue, num)

while queue:
    now = heapq.heappop(queue)
    topological_sorted.append(str(now))

    # 현재 문제와 연결된 문제들의 진입차수를 1 감소시키고,
    for node in graph[now]:
        in_deg[node] -= 1

        # 진입차수가 0이 된 문제가 있는경우, 해당 문제 번호를 우선순위 큐에 삽입한다.
        if in_deg[node] == 0:
            heapq.heappush(queue, node)

print(" ".join(topological_sorted))
