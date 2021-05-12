# 9465 : 스티커
#
# 2행 N열의 스티커들에 배정된 점수를 최대로 하기 위해서는, 첫 번째열부터 N 번째열까지 DP 배열을 생성해야 한다.
#
# 첫 번째와 두 번째 열의 경우, 단순히 대각선에 위치한 스티커 점수를 DP 배열에 저장하면 된다.
#
# 세 번째 열부터는, 두 가지 경우의 수 1) 바로 앞 열 대각선 스티커, 2) 두 열 앞 대각선 스티커 중 최대값을 선택해야 한다.
#
# 마지막 열까지 진행한 후, 마지막 열의 DP 배열 값 중 최대값을 출력하면 된다.

from sys import stdin

T = int(stdin.readline().rstrip())
for _ in range(T):
    N = int(stdin.readline().rstrip())
    DP = [[0 for _ in range(N)] for _ in range(2)]
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, stdin.readline().rstrip().split())))

    DP[0][0] = sticker[0][0]
    DP[1][0] = sticker[1][0]
    DP[0][1] = DP[1][0] + sticker[0][1]
    DP[1][1] = DP[0][0] + sticker[1][1]

    for index in range(2, N):
        DP[0][index] = max(DP[1][index - 1], DP[1][index - 2]) + sticker[0][index]
        DP[1][index] = max(DP[0][index - 1], DP[0][index - 2]) + sticker[1][index]

    print(max(DP[0][N - 1], DP[1][N - 1]))