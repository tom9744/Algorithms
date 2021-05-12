n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    DP = [0 for _ in range(n + 1)]
    DP[1], DP[2] = 1, 3

    for i in range(3, n + 1):
        DP[i] = (DP[i - 1] + (DP[i - 2] * 2)) % 10007

    print(DP[n])
