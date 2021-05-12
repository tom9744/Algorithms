# 2167 : 2차원 배열의 합
#
# 단순 반복문으로 풀이한 경우 Python3에서는 시간초과가 나서 DP로 풀이하는 방법도 찾아봤는데,
# 뭔가 구현을 잘못한 것인지 DP로 풀어도 Pypy3 에서만 통과가 된다...


def get_sum(arr, x, y):
    result = 0
    for row in range(0, x):
        result += sum(array[row][0:y])
    return result


N, M = map(int, input().split())
array = []
dp = [[0 for _ in range(M + 1)]for _ in range(N + 1)]

for _ in range(N):
    array.append(list(map(int, input().split())))

# DP 배열 생성
for x in range(1, N + 1):
    for y in range(1, M + 1):
        dp[x][y] = get_sum(array, x, y)

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())

    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])


# Python3 시간초과, Pypy3 통과
# for _ in range(K):
#     i, j, x, y = map(int, input().split())
#     result = 0
#
#     for row in range(i - 1, x):
#         result += sum(array[row][j-1:y])
#     print(result)