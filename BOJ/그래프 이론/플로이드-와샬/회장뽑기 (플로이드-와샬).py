import sys
input = sys.stdin.readline

N = int(input())
INF = float("inf")

# 인접 행렬 방식으로 그래프를 표현한다. (자기자신은 0으로 초기화)
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for n in range(N + 1):
    graph[n][n] = 0

while True:
    src, dst = map(int, input().split())

    if src == -1 and dst == -1:
        break

    graph[src][dst] = 1
    graph[dst][src] = 1

# 플로이드-와샬 알고리즘을 이용해, 각 회원 사이의 거리를 구한다.
for n in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][n] + graph[n][j])

scores = []
min_score = INF

# 각 회원의 점수를 확인하고, 최소 점수를 구한다.
for n in range(1, N + 1):
    score = max(graph[n][1:])  # 각 회원의 점수는 행의 최대값이다.
    min_score = min(min_score, score)
    scores.append(score)

candidates = [str(num + 1) for num in range(N) if scores[num] == min_score]

print(min_score, len(candidates))
print(" ".join(candidates))
