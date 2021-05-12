# 11047 : 동전 0

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

counter = 0
num_of_coins = 0

while k is not 0:
    divided_by_current_coin = k // coins[n - 1 - counter]

    if divided_by_current_coin > 0:
        num_of_coins += divided_by_current_coin

        leftover = k % coins[n - 1 - counter]

        k = leftover
    else:
        counter += 1

print(num_of_coins)
