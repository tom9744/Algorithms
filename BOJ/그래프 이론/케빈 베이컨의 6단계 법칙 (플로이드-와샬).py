INF = float("inf")
N, M = map(int, input().split())

# 친구 관계 그래프를 인접 행렬로 나타낸다.
relationship = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기자신과의 관계는 0으로 초기화한다.
for idx in range(1, N + 1):
    relationship[idx][idx] = 0

# 친구 관계를 입력받아, 그래프에 반영한다. (가중치 없는 무방향 그래프)
for _ in range(M):
    A, B = map(int, input().split())
    relationship[A][B] = 1
    relationship[B][A] = 1

# 플로이드 와샬 알고리즘을 이용해, 다른 사람과 연결되기 위해 필요한 최소 단계를 구한다.
for n in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            relationship[i][j] = min(relationship[i][j],
                                     relationship[i][n] + relationship[n][j])

min_kevin_bacon = float("inf")
result = 0
# 가장 작은 케빈 베이컨 수를 구한다.
for i in range(1, N + 1):
    kevin_bacon = sum(relationship[i][1:])

    if kevin_bacon < min_kevin_bacon:
        min_kevin_bacon = kevin_bacon
        result = i

print(result)