# 2579 : 계단 오르기
#
# 계단을 오르는 두 가지 경우의 수 1) 한 칸, 2) 두 칸 일 때, 첫 번째 경우에 대해서는 추가적인 검증이 필요하다.
# 문제의 조건에 따라 '연속된 세 칸을 밟은 수 없도록' 해야하기 때문이다.
#
# 마찬가지로 DP 개념을 도입해 각 계단에 도달할 수 있는 최대값을 시작부터 누적하여 저장한다.
# 점화식은 DP[i] = DP[i - 2] + stair[i] 또는 DP[i] = DP[i - 3] + stair[i - 1] + stair[i]인데,
# DP[i] = DP[i - 3] + stair[i - 1] + stair[i]는 연속적으로 세 칸을 밟지 못하도록 하기 위한 점화식이다.

N = int(input())
scores = [0 for _ in range(N + 1)]
DP = [0, ]
for index in range(1, N + 1):
    scores[index] = int(input())

if N == 1:
    print(scores.pop())
else:
    # 1칸 이동, 2칸 이동하는 경우 중 큰 값을 선택
    DP.append(max(scores[0], scores[0] + scores[1]))
    DP.append(max(scores[0] + scores[2], scores[1] + scores[2]))

    for stair in range(3, N + 1):
        DP.append(max(DP[stair - 2] + scores[stair], DP[stair - 3] + scores[stair - 1] + scores[stair]))

    print(DP.pop())
