def solution(n):
    DP = [0 for _ in range(n + 1)]
    DP[0], DP[1] = 0, 1

    for idx in range(2, n + 1):
        DP[idx] = (DP[idx - 1] + DP[idx - 2]) % 1234567

    return DP[-1]