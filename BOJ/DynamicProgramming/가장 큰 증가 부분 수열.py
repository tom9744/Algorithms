# 11055: 가장 큰 증가 부분 수열

N = int(input())
DP = [0 for _ in range(N)]
permutations = list(map(int, input().split()))

DP[0] = permutations[0]

for i in range(1, N):
    for j in range(i):
        if permutations[i] > permutations[j]:
            DP[i] = max(DP[i], DP[j] + permutations[i])
        else:
            DP[i] = max(DP[i], permutations[i])

print(max(DP))
