# 9465: 스티커

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))

    DP = [[0] * n for _ in range(2)]
    DP[0][0], DP[1][0] = stickers[0][0], stickers[1][0]

    for index in range(1, n):
        # N이 1인 경우, N-1일 때 대각선 위치의 스티커 점수 + 현재 스티커 점수
        if index < 2:
            DP[0][index] = DP[1][index - 1] + stickers[0][index]
            DP[1][index] = DP[0][index - 1] + stickers[1][index]
        # N이 2 이상인 경우, N-1, N-2일 때 대각선 위치의 스티커 점수 중 큰 값 + 현재 스티커 점수
        else:
            DP[0][index] = max(DP[1][index - 1], DP[1][index - 2]) + stickers[0][index]
            DP[1][index] = max(DP[0][index - 1], DP[0][index - 2]) + stickers[1][index]

    # N일 때 첫번째 줄, 두번째 줄에 누적된 값을 비교하여, 큰 값을 출력한다.
    print(max(DP[0][n - 1], DP[1][n - 1]))
