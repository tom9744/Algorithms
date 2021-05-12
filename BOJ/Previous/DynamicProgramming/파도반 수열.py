T = int(input())

for _ in range(T):
    N = int(input())
    DP = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    if N > 9:
        for index in range(10, N):
            DP.append(DP[index - 5] + DP[index - 1])

    print(DP[N - 1])
