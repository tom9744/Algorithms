import sys
input = sys.stdin.readline

N, K = map(int, input().split())
INF = float("inf")

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for idx in range(1, N + 1):
    graph[idx][idx] = 0

for _ in range(K):
    early, late = map(int, input().split())
    graph[early][late] = 1

for n in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][n] + graph[n][j])

S = int(input())

for _ in range(S):
    case_1, case_2 = map(int, input().split())

    # 두 사건이 연결되어 있지 않는 경우, 선후관계를 알 수 없다
    if graph[case_1][case_2] == INF and graph[case_2][case_1] == INF:
        print(0)
    # case_1에서 case_2로만 이어져 있는 경우, case_1이 먼저 일어난 사건이다.
    elif graph[case_1][case_2] != INF and graph[case_2][case_1] == INF:
        print(-1)
    # case_2에서 case_1로만 이어져 있는 경우, case_2가 먼저 일어난 사건이다.
    elif graph[case_1][case_2] == INF and graph[case_2][case_1] != INF:
        print(1)
