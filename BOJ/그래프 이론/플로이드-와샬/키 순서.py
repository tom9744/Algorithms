import sys
input = sys.stdin.readline

INF = float("inf")
N, M = map(int, input().split())

graph = [[INF] * (N + 1) for _ in range(N + 1)]
for idx in range(1, N + 1):
    graph[idx][idx] = 0

for _ in range(M):
    short, tall = map(int, input().split())
    graph[short][tall] = 1

# 플로이드 와샬 알고리즘을 이용해, 모든 노드에 대한 최단 거리를 계산한다.
for n in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][n] + graph[n][j])

count = [0] * (N + 1)

# 특정 노드에서 다른 노드로 갈 수 있는 경우(= 플로이드 와샬 결과가 0이나 무한대(INF)가 아닌 경우),
# 다른 노드에서 특정 노드로 갈 수 있는 경우를 모두 합쳐서 N - 1이 나오면 순서를 알 수 있다.
for n in range(1, N + 1):
    for i in range(1, N + 1):
        # 특정 노드 n에서 다른 노드로 이동할 수 있는 경우의 수를 센다.
        if 0 < graph[n][i] < INF:
            count[n] += 1
        # 다른 노드에서 특정 노드 n으로 이동할 수 있는 경우의 수를 센다.
        if 0 < graph[i][n] < INF:
            count[n] += 1

print(count.count(N - 1))