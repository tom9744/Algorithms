# 9095 : 1, 2, 3 더하기
#
# 점화식을 구해서 푸는 문제다.
# 정수 N이 3보다 클 때, solution(N) = solution(N - 1) + solution(N - 2) + solution(N - 3)이 성립한다.

T = int(input())


def solution(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    return solution(N - 1) + solution(N - 2) + solution(N - 3)


for _ in range(T):
    N = int(input())

    print(solution(N))
