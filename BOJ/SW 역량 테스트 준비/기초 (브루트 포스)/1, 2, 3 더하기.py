T = int(input())

for _ in range(T):
    N = int(input())

    if N == 1:
        print(1)
    elif N == 2:
        print(2)
    elif N == 3:
        print(4)
    else:
        DP = [0 for _ in range(N + 1)]
        DP[1], DP[2], DP[3] = 1, 2, 4

        for n in range(4, N + 1):
            DP[n] = DP[n - 1] + DP[n - 2] + DP[n - 3]

        print(DP[N])
        