# 11052 : 카드 구매하기
#
# N개의 카드를 구매하는 방법은 (N팩), (1팩 + N-1팩), (2팩 + N-2팩), (3팩 + N-3팩)...과 같다.
#
# 예를 들어, 3개의 카드를 구매하는 방법은 3팩, 2팩 + 1팩, 1팩 + 1팩 + 1팩이다.
# 그런데 여기서 2팩 + 1팩, 1팩 + 1팩 + 1팩은 (2개의 카드를 구매하는 방법 + 1개의 카드를 구매하는 방법)이다.
#
# 3개의 카드를 구매하는 방법 중 가격을 가장 비싸게 구매해야 하므로,
# 3팩, 2팩 + 1팩, 1팩 + 1팩 + 1팩의 세 가지 경우의 수 중 가격이 가장 비싼 것을 고르면 된다.
#
# 즉, DP[N] = max(DP[N], DP[i] + DP[N - i])를 반복해 최대값을 구하면 된다.

N = int(input())  # 구매할 카드의 개수
prices = [0]
prices.extend(list(map(int, input().split())))  # 카드팩 가격

DP = [0 for _ in range(N + 1)]
DP[1] = prices[1]
DP[2] = max(prices[2], DP[1] * 2)

for card in range(3, N + 1):
    DP[card] = prices[card]
    for index in range(1, N // 2 + 1):
        DP[card] = max(DP[card], DP[index] + DP[card - index])

print(DP[N])