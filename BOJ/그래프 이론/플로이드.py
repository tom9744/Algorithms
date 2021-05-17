import sys
input = sys.stdin.readline

INF = float("inf")
N = int(input())
M = int(input())

# 도시를 인접 그래프 형태로 나타낸다.
cities = [[INF] * N for _ in range(N)]
for n in range(N):
    cities[n][n] = 0

# 버스 노선 정보에 따라 그래프를 갱신한다.
for _ in range(M):
    start, end, price = map(int, input().split())
    # 시작 도시와 도착 도시를 연결하는 노선이 하나 이상인 경우, 최소값을 선택한다.
    cities[start - 1][end - 1] = min(cities[start - 1][end - 1], price)

# 플로이드 와샬 알고리즘을 수행하여, 최단 거리를 구한다.
for n in range(N):
    for i in range(N):
        for j in range(N):
            cities[i][j] = min(cities[i][j], cities[i][n] + cities[n][j])

for i in range(N):
    for j in range(N):
        if cities[i][j] == INF:
            print(0, end=" ")
        else:
            print(cities[i][j], end=" ")
    print()
