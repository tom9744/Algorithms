# 11726: 2xN 타일링

N = int(input())

if 1 <= N < 3:
    print(N)
else:
    DP = [0 for _ in range(N + 1)]
    DP[1], DP[2] = 1, 2

    for n in range(3, N + 1):
        DP[n] = (DP[n - 1] + DP[n - 2]) % 10007

    print(DP[N])
