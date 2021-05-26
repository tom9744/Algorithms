N = int(input())
M = int(input())
INF = float("inf")

graph = [[INF] * (N + 1) for _ in range(N + 1)]
# 자기 자신으로의 거리는 0으로 초기화한다.
for idx in range(1, N + 1):
    graph[idx][idx] = 0

# 노드 연결 정보를 입력 받는다.
for _ in range(M):
    heavy, light = map(int, input().split())
    graph[heavy][light] = 1

# 플로이드-와샬 알고리즘 수행
for n in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][n] + graph[n][j])

for num in range(1, N + 1):
    # 현재 물건보다 가벼운 물건 파악 가능 여부
    lighter_than_current = graph[num][1:]
    # 현재 물건보다 무거운 물건 파악 가능 여부
    heavier_than_current = [graph[i][num] for i in range(1, N + 1)]

    cannot_know = 0

    # 둘 다 'INF'인 경우, 대/소 관계를 알 수 없는 것이다.
    for idx in range(N):
        if lighter_than_current[idx] == INF and \
                heavier_than_current[idx] == INF:
            cannot_know += 1

    print(cannot_know)
