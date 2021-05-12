# 16194: 카드 구매하기 2

N = int(input())
prices = list(map(int, input().split()))
DP = [0 for _ in range(N)]

for i in range(N):
    DP[i] = prices[i]
    for j in range(i):
        # (카드 N-i개를 구매한 최대 가격 + 카드 i개를 구매하는 가격)과
        # 카드 N개를 구매한 현재의 최대 가격을 비교해, 더 큰 값을 DP[i]에 넣는다.
        DP[i] = max(DP[i], DP[j] + prices[i - j - 1])

print(DP[N - 1])
