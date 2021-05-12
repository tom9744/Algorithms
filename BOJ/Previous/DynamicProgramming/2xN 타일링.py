# 11726 : 2xN 타일링
#
# N = 1부터 N = 6 정도까지 2x1, 1x2 타일로 2xN 공간을 채울 수 있는 경우의 수를 세어보면,
# DP[N] = DP[N - 1] + DP[N - 2] (N > 2)와 같은 점화식을 구할 수 있으며, 이 점화식을 적용하면 된다

N = int(input())
DP = [0 for _ in range(N + 1)]

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    DP[1], DP[2] = 1, 2

    for idx in range(3, N + 1):
        DP[idx] = DP[idx - 1] + DP[idx - 2]

    print(DP[N] % 10007) 