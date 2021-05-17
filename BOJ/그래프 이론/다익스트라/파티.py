import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
INF = float("inf")

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    src, end, dist = map(int, input().split())
    graph[src].append((end, dist))


# 다익스트라 알고리즘을 통해, 주어진 시작점에서 모든 노드로 가는 최단 거리를 구한다.
def dijkstra(start):
    distance = [INF for _ in range(N + 1)]
    p_queue = []

    heapq.heappush(p_queue, (0, start))
    distance[start] = 0

    while p_queue:
        current_dist, current_node = heapq.heappop(p_queue)

        if distance[current_node] < current_dist:
            continue

        for node, dist in graph[current_node]:
            new_dist = current_dist + dist

            if new_dist < distance[node]:
                distance[node] = new_dist
                heapq.heappush(p_queue, (new_dist, node))

    return distance


# 각 학생에 대해, N번째 마을에서 X번째 마을로 가는 최단 거리를 구한다.
to_X = [dijkstra(n)[X] for n in range(N + 1)]
# X번 마을에서 각 학생들이 속한 N번째 마을로 돌아가는 최단 거리를 구한다.
from_X = dijkstra(X)

# 학생이 N번째 마을에서 X번 마을로 가는 최단거리와
# X번 마을에서 N번째 마을로 가는 최단거리를 합하고, 최대값을 찾는다.
result = 0
for i in range(1, N + 1):
    result = max(result, to_X[i] + from_X[i])
print(result)