# 11055: 가장 큰 증가 부분 수열

N = int(input())
permutation = list(map(int, input().split()))
DP = [0 for _ in range(N)]

for curr in range(N):
    DP[curr] = permutation[curr]
    for num in range(curr):
        if permutation[num] < permutation[curr]:
            DP[curr] = max(DP[num] + permutation[curr], DP[curr])

print(max(DP))
