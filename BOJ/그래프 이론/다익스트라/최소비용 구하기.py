import heapq
import sys
input = sys.stdin.readline

INF = float("inf")
N = int(input())  # 도시 개수
M = int(input())  # 버스 개수

graph = [[] for _ in range(N + 1)]
cost_table = [INF for _ in range(N + 1)]

for _ in range(M):
    start, dest, cost = map(int, input().split())
    graph[start].append((dest, cost))


# 다익스트라 알고리즘을 이용해, 주어진 시작점에서 모든 노드로 이동하는 최단 거리를 구한다.
def dijkstra(start):
    p_queue = []
    heapq.heappush(p_queue, (0, start))
    cost_table[start] = 0

    while p_queue:
        current_cost, current_node = heapq.heappop(p_queue)

        if cost_table[current_node] < current_cost:
            continue

        for node, cost in graph[current_node]:
            new_cost = current_cost + cost

            if new_cost < cost_table[node]:
                cost_table[node] = new_cost
                heapq.heappush(p_queue, (new_cost, node))


start_node, dest_node = map(int, input().split())

dijkstra(start_node)  # 최단 거리를 구한다.

print(cost_table[dest_node])  # 목표 지점까지의 거리를 출력한다.
