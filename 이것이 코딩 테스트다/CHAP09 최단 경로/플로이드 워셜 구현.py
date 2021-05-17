INF = int(1e9)

N = int(input())  # 노드의 개수
M = int(input())  # 간선의 개수

# 그래프를 인접 행렬로 구현하고, 모두 무한(INF)으로 초기화
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(M):
    src, dest, weight = map(int, input().split())
    graph[src][dest] = weight

# 점화식에 따라, 플로이드 워셜 알고리즘 수행
for n in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # 해당 노드를 통해 가는 경우와, 그렇지 않은 경우 중 작은 비용을 선택
            graph[i][j] = min(graph[i][j], graph[i][n] + graph[n][j])

# 수행된 결과를 출력
for i in range(1, N + 1):
    for j in range(1, N + 1):
        # 도달할 수 없는 경우, "INF"로 출력
        if graph[i][j] == INF:
            print("INF", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

# 입력
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
# 출력
# 0 4 8 6
# 3 0 7 9
# 5 9 0 4
# 7 11 2 0

