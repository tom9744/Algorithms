import heapq
import sys
input = sys.stdin.readline

INF = float("inf")
V, E = map(int, input().split())
K = int(input())  # 시작 지점

graph = [[] for _ in range(V + 1)]
distance = [INF for _ in range(V + 1)]

# 그래프 연결 상태를 입력 받는다. (방향 그래프)
for _ in range(E):
    src, to, weight = map(int, input().split())
    graph[src].append([to, weight])


def dijkstra(start):
    p_queue = []
    heapq.heappush(p_queue, (0, start))  # 시작점을 우선순위 큐에 삽입한다.
    distance[start] = 0  # 시작점에서 시작점으로의 거리는 0이다.

    while p_queue:
        current_dist, current_vertex = heapq.heappop(p_queue)

        # 이미 방문한 적이 있는 경우 무시한다.
        # WHY? 다익스트라 수행 시, 한번 선택한 노드는 이미 최단 거리가 결정된다.
        if distance[current_vertex] < current_dist:
            continue

        for vertex, dist in graph[current_vertex]:
            new_dist = current_dist + dist

            # 현재 노드를 거쳐서 연결된 노드로 이동하는 거리가 더 짧은 경우, 거리 테이블을 갱신한다.
            if new_dist < distance[vertex]:
                distance[vertex] = new_dist
                # 갱신된 최단 거리로 우선순위 큐에 새롭게 삽입한다.
                heapq.heappush(p_queue, (new_dist, vertex))


dijkstra(K)

for i in range(1, V + 1):
    if distance[i] < INF:
        print(distance[i])
    else:
        print("INF")