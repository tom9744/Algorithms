T = int(input())

for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    portfolio = []
    continuous = []

    prev = prices.pop(0)
    continuous.append(prev)
    for price in prices:
        now = price

        if prev <= now:
            continuous.append(now)
            prev = now
        else:
            continuous.append(now)
            portfolio.append(continuous)
            continuous = []
            prev = now

        print(continuous)
