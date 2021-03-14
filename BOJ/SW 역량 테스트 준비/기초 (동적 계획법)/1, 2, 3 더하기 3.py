# 15988: 1, 2, 3 더하기 3

T = int(input())

# 테스트 케이스마다 DP 배열을 다시 구하지 않고,
# 처음부터 구해놓고 재사용하면 시간을 줄일 수 있다.
DP = [0 for _ in range(1000001)]
DP[1], DP[2], DP[3] = 1, 2, 4

for num in range(4, 1000001):
    DP[num] = (DP[num - 1] + DP[num - 2] + DP[num - 3]) % 1000000009

for _ in range(T):
    n = int(input())

    if n < 3:
        print(n)
    elif n == 3:
        print(4)
    else:
        print(DP[n])
