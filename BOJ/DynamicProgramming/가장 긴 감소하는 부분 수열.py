# 11722: 가장 긴 감소하는 부분 수열
#
# N번째 수에 대해 첫번째부터 N-1번째 수와 비교하면서 N번째 수보다 큰 수가 있는 경우,
# DP[i] = max(DP[j] + 1, DP[i])를 수행해 N번째 수까지 이어지는 가장 긴 감소하는 부분 수열의 길이를 구한다.
#
# 단순히 DP[i] = DP[j] + 1 만 수행하면, 만약 30, 40, 20 일때 정답이 2인데 출력이 3이 되게 된다.
# 즉, 40이 수열에 포함되지 않도록 하는 처리를 해주는 것이다.

N = int(input())
DP = [1 for _ in range(N)]
permutations = list(map(int, input().split()))

for i in range(1, N):
    for j in range(i):
        if permutations[j] > permutations[i]:
            DP[i] = max(DP[j] + 1, DP[i])

print(max(DP))