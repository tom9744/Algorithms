# 1463: 1로 만들기
#
# 주어진 세 가지 방법을 사용해 현재 수를 만들 수 있는 경우 중,
# DP 배열에 누적된 값이 가장 적은 것에 +1 해주면 된다.
#
# 즉, DP[N]일 때 DP[N // 3], DP[N // 2], DP[N -1]의 값들에서
# 가장 작은 수에 +1 하면된다. (다만, 나누어 떨어지지 않는 경우는 제외)

from sys import maxsize

N = int(input())

if N == 1:
    print(0)
elif 1 < N < 4:
    print(1)
else:
    DP = [0 for _ in range(N + 1)]
    DP[1], DP[2], DP[3] = 0, 1, 1

    for number in range(4, N + 1):
        minimum = maxsize
        if number % 3 == 0:
            minimum = min(minimum, DP[number // 3])
        if number % 2 == 0:
            minimum = min(minimum, DP[number // 2])

        minimum = min(minimum, DP[number - 1])

        DP[number] = minimum + 1

    print(DP[N])
