import heapq
import sys
input = sys.stdin.readline

INF = float("inf")
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]

for _ in range(M):
    src, dst = map(int, input().split())
    graph[src].append((dst, 1))


def dijkstra(start):
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


# 출발 도시 X에서 다른 도시로 가는 최단 거리를 구한다.
dijkstra(X)

result = []
# 최단 거리가 K인 도시의 번호를 배열에 담는다.
for number, dist in enumerate(distance):
    if dist == K:
        result.append(number)

# 배열에서 하나씩 꺼내 출력한다.
if len(result) > 0:
    for node in result:
        print(node)
# 배열이 비어있는 경우, 최단 거리 K인 도시가 없으므로 -1을 출력한다.
else:
    print(-1)
