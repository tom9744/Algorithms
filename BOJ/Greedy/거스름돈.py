# 1931 : 거스름돈

amount_of_change = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coins:
    num_of_coins = amount_of_change // coin

    count += num_of_coins if num_of_coins > 0 else 0

    amount_of_change = amount_of_change % coin

    if amount_of_change is 0:
        break

print(count)