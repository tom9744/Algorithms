import sys
input = sys.stdin.readline

V, E = map(int, input().split())
INF = float("inf")

# 인접 행렬로 그래프를 나타내며, 거리는 모두 무한대로 초기화한다.
graph = [[INF] * (V + 1) for _ in range(V + 1)]

# 간선 및 비용 정보를 입력받는다. (방향 그래프)
for _ in range(E):
    src, dst, cost = map(int, input().split())
    graph[src][dst] = cost

# 플로이드 와샬 알고리즘을 수행하여, 각 노드에서 다른 노드로 가는 모든 최소비용을 구한다.
for n in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            graph[i][j] = min(graph[i][j], graph[i][n] + graph[n][j])

min_cost = INF
# 모든 노드에 대해 왕복 비용을 확인하고, 최소값을 찾는다.
for i in range(1, V + 1):
    for j in range(1, V + 1):
        outbound = graph[i][j]  # 현재 지점에서 목표 지점까지의 최단거리
        inbound = graph[j][i]   # 목표 지점에서 현재 지점까지의 최단거리
        min_cost = min(min_cost, outbound + inbound)

if min_cost < INF:
    print(min_cost)
else:
    print(-1)
