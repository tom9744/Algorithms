N = int(input())
INF = float("inf")

graph = [[INF for _ in range(N)] for _ in range(N)]

# 문제의 조건에 따라 자기자신으로 이동할 수 없으므로, i와 j가 같아도 0으로 설정하지 않는다.
for i in range(N):
    for j, is_connected in enumerate(input().split()):
        # 연결된 노드의 경우, 거리를 1로 설정한다. (가중치 없는 방향 그래프)
        if is_connected == "1":
            graph[i][j] = 1

# 플로이드 와샬 알고리즘을 수행하여, 모든 노드에 대해 최단 거리를 구한다.
for n in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][n] + graph[n][j])

for i in range(N):
    for j in range(N):
        # 최단거리가 무한(INF)보다 작으면, 경로가 존재하는 것이다.
        if graph[i][j] < INF:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
