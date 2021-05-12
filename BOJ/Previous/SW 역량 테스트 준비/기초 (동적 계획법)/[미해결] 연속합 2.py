# 13398: 연속합 2

n = int(input())
permutation = list(map(int, input().split()))
DP = [[0] * n for _ in range(2)]
DP[0][0] = permutation[0]
DP[1][0] = permutation[0]

for num in range(1, n):
    DP[0][num] = max(permutation[num], DP[0][num - 1] + permutation[num])
    DP[1][num] = max(DP[0][num - 1], DP[1][num - 1] + permutation[num])

maxA = max(DP[0])
maxB = max(DP[1])

print(max(maxA, maxB))
