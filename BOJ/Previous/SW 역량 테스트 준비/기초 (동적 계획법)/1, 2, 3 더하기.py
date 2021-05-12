# 9095: 1, 2, 3 더하기
#
# 기본적으로는 동적 계획법 또는 완전 탐색을 사용해 풀 수 있는 문제이지만,
# 주어지는 정수 'n'의 범위가 1~10으로 굉장히 좁으므로
# 모든 경우의 수에 대해 직접 값을 구해 출력하는 것이 시간/메모리 차원에서 압도적이다.

T = int(input())

for _ in range(T):
    n = int(input())

    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    elif n == 4:
        print(7)
    elif n == 5:
        print(13)
    elif n == 6:
        print(24)
    elif n == 7:
        print(44)
    elif n == 8:
        print(81)
    elif n == 9:
        print(149)
    elif n == 10:
        print(274)

# 동적 계획법을 이용한 풀이
#
# T = int(input())
#
# for _ in range(T):
#     N = int(input())
#
#     if N == 1:
#         print(1)
#     elif N == 2:
#         print(2)
#     elif N == 3:
#         print(4)
#     else:
#         DP = [0 for _ in range(N + 1)]
#         DP[1], DP[2], DP[3] = 1, 2, 4
#
#         for n in range(4, N + 1):
#             DP[n] = DP[n - 1] + DP[n - 2] + DP[n - 3]
#
#         print(DP[N])
