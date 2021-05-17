import heapq

N, M, C = map(int, input().split())
INF = float("inf")

graph = [[] for _ in range(N)]
distances = [INF for _ in range(N)]

for _ in range(M):
    src, dest, cost = map(int, input().split())
    graph[src - 1].append((dest - 1, cost))


def dijkstra(start):
    queue = []
    # 시작점에서 시작점으로 가는 비용은 0이다.
    heapq.heappush(queue, (0, start))
    distances[start] = 0

    while queue:
        current_cost, current_node = heapq.heappop(queue)
        # 이미 처리한 노드인 경우, 생략한다.
        if distances[current_node] < current_cost:
            continue

        for node, cost in graph[current_node]:
            new_cost = current_cost + cost

            # 현재 노드를 거쳐 다음 노드로 이동하는 비용이 더 적다면, 거리 테이블을 갱신한다.
            if new_cost < distances[node]:
                distances[node] = new_cost
                heapq.heappush(queue, (new_cost, node))


dijkstra(C - 1)

city_count, max_cost = 0, 0
for idx, dist in enumerate(distances):
    # 방문할 수 있는 것으로 판명된 도시인 경우,
    if dist < INF:
        city_count += 1
        max_cost = max(max_cost, dist)

# 시작 지점은 제외한다.
print(city_count - 1, max_cost)

# 입력
# 3 2 1
# 1 2 4
# 1 3 2
# 출력
# 2 4
