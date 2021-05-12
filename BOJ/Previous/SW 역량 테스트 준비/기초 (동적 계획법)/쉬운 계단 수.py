N = int(input())

DP = [[0] * 10 for _ in range(N + 1)]
DP[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for n in range(2, N + 1):
    for num in range(10):
        if num == 0:
            DP[n][num] = DP[n - 1][num + 1]
        elif 0 < num < 9:
            DP[n][num] = DP[n - 1][num - 1] + DP[n - 1][num + 1]
        elif num == 9:
            DP[n][num] = DP[n - 1][num - 1]

result = sum(DP[N]) - DP[N][0]
print(result % 1000000000)
