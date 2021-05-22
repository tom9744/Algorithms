import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
INF = float("inf")

graph = [[] for _ in range(N + 1)]

# 간선 및 비용 정보를 입력 받는다. (무방향 그래프)
for _ in range(E):
    src, dst, dist = map(int, input().split())
    graph[src].append((dst, dist))
    graph[dst].append((src, dist))


def dijkstra(start):
    distance = [INF for _ in range(N + 1)]
    queue = []

    heapq.heappush(queue, (0, start))  # 시작노드를 우선순위 큐에 삽입한다. (비용 = 0)
    distance[start] = 0

    while queue:
        now_dist, now_node = heapq.heappop(queue)

        if distance[now_node] < now_dist:
            continue

        for node, dist in graph[now_node]:
            new_dist = now_dist + dist

            if new_dist < distance[node]:
                distance[node] = new_dist
                heapq.heappush(queue, (new_dist, node))

    return distance


v1, v2 = map(int, input().split())

from_start = dijkstra(1)     # 시작점에서의 최단거리
from_vertex1 = dijkstra(v1)  # V1에서의 최단거리
from_vertex2 = dijkstra(v2)  # V2에서의 최단거리

# 특정한 경로를 통해 N에 도착하는 두 경우의 수 중 최소값을 구한다.
min_distance = min(
    from_start[v1] + from_vertex1[v2] + from_vertex2[N],  # 1 -> V1 -> V2 -> N
    from_start[v2] + from_vertex2[v1] + from_vertex1[N]   # 1 -> V2 -> V1 -> N
)

if min_distance < INF:
    print(min_distance)
else:
    print(-1)
