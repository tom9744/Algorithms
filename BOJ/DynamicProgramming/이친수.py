# 2193 : 이친수
#
# 간단한 DP 문제로, N = 6 정도까지 직접 경우의 수를 구해보면 점화식을 구할 수 있다.
# 점화식은 DP[index] = DP[index - 1] + DP[index - 2]로, 피보나치 수열이다.

N = int(input())
DP = [0 for _ in range(N + 1)]

if N < 3:
    print(1)
else:
    DP[1] = 1
    DP[2] = 1

    for index in range(3, N + 1):
        DP[index] = DP[index - 1] + DP[index - 2]

    print(DP[N])