# 11722: 가장 긴 감소하는 부분 수열
#
# [11053: 가장 긴 증가하는 부분 수열]에서 부등호 방향만 바뀐 문제이다.

N = int(input())
DP = [1 for _ in range(N)]
permutation = list(map(int, input().split()))

for curr in range(N):
    for num in range(curr):
        if permutation[num] > permutation[curr]:
            DP[curr] = max(DP[curr], DP[num] + 1)

print(max(DP))