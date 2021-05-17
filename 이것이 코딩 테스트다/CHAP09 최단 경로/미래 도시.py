INF = float("inf")
N, M = map(int, input().split())

# 2차원 그래프을 무한대로 초기화한다.
graph = [[INF for _ in range(N)] for _ in range(N)]

# 자기자신으로 가는 비용은 0으로 설정한다.
for x in range(N):
    for y in range(N):
        if x == y:
            graph[x][y] = 0

# 경로를 입력 받고, 정해진 거리(= 1)로 설정한다.
for _ in range(M):
    src, dest = map(int, input().split())
    # 무방향 그래프이므로, 양방향 모두 1로 설정해야 한다.
    graph[src - 1][dest - 1] = 1
    graph[dest - 1][src - 1] = 1

# 플로이드 워셜 알고리즘을 수행해 모든 노드에 대한 최단 거리를 구한다.
for n in range(N):
    for x in range(N):
        for y in range(N):
            graph[x][y] = min(graph[x][y], graph[x][n] + graph[n][y])

X, K = map(int, input().split())  # K번 회사를 거쳐, X번 회사에 도착해야 한다.

# 0번 회사 -> K번 회사 -> X번 회사로 이동하는 최단거리를 계산한다.
if graph[0][K - 1] + graph[K - 1][X - 1] < INF:
    print(graph[0][K - 1] + graph[K - 1][X - 1])
else:
    print(-1)

# 입력
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# 출력
# 3
