# 2225: 합분해

N, K = map(int, input().split())

if K == 1:
    print(1)
elif K == 2:
    print(N + 1)
else:
    DP = [[0] * (N + 1) for _ in range(K + 1)]
    DP[1] = [1 for _ in range(N + 1)]
    DP[2] = [(num + 1) for num in range(N + 1)]

    for num in range(3, K + 1):
        for i in range(N + 1):
            for j in range(i + 1):
                DP[num][i] += DP[num - 1][i - j]
            DP[num][i] %= 1000000000

    print(DP[K][N])