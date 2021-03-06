# 11057: 오르막 수
#
# 숫자가 0일때 두 자리의 오르막 수로 만드는 방법은 0~9까지의 수 10개를 뒤에 붙이는 것이다.
# 숫자가 5일때 두 자리의 오르막 수로 만드는 방법은 5~9까지의 수 5개를 뒤에 붙이는 것이다.
# 이런 방식으로 각 한 자리 숫자에서 두 자리의 오르막 수를 만들 수 있는 방법의 개수는
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 개이다. (총 55개)
#
# 두 자리에서 세 자리 오르막 수를 만드는 과정도 동일하게 생각하면 된다.
# 00이라는 두 자리 오르막 수에서 세 자리 오르막 수를 만들 수 있는 방법은
# 000, 001, 002, 003, ..., 009 이런 식이다.
#
# 즉, DP[n][number] = sum(DP[n - 1][number:])인 것이다.

N = int(input())
DP = [[0] * 10 for _ in range(N + 1)]
DP[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for n in range(2, N + 1):
    for number in range(10):
        DP[n][number] = sum(DP[n - 1][number:])

print(sum(DP[N]) % 10007)
