# 2293 : 동전 1
#
# 1, 2, 5원 동전을 사용해 10원을 만드는 것은 5원, 8원, 9원을 만드는 경우의 수 의 합이다.
# 즉, DP[10] = DP[5] + DP[8] + DP[9]와 같은 식이 성립한다.
#
# 위와 같은 점화식을 DP 배열을 통해 구현하기 위해 각 동전을 사용해 1원부터 K원을 만들 수 있는 경우의 수를 배열에 담는다.
# 1원으로 1원부터 10원을 만들 수 있는 경우의 수를 먼저 구하고,
# 이어서 2원으로 2원부터 10원을 만들 수있는 경우의 수, 5원으로 5원부터 10원을 만들 수 있는 경우의 수를 DP 배열에 누적한다.
#
# 이 때, 동전 하나만을 이용하는 경우를 위해 DP[0]의 값은 1로 미리 지정해 놓아야 한다.

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

DP = [0 for _ in range(K + 1)]
DP[0] = 1

for coin in coins:
    for price in range(coin, K + 1):
        DP[price] += DP[price - coin]

print(DP[K])