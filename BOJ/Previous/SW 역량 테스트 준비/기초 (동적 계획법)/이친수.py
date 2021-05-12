N = int(input())

if N < 3:
    print(1)
else:
    DP = [0 for _ in range(N + 1)]
    DP[1], DP[2] = 1, 1

    for n in range(3, N + 1):
        DP[n] = DP[n - 1] + DP[n - 2]

    print(DP[N])