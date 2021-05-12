# 1912 : 연속합
#
# 맨 앞부터 수열의 수를 하나씩 방문한다.
# 이때, "현재까지의 누적합 + 현재 수"와 "현재 수"의 크기를 비교한다.
#
# "현재까지의 누적합 + 현재 수"가 "현재 수"보다 크다면, DP 배열의 현재 위치 인덱스에 "현재까지의 누적합 + 현재수"를 반영한다.
# (즉, 계속해서 수를 더해 나가는 것이다.)
#
# "현재 수"가 단독으로 더 크다면, 지금까지 누적한 값을 버리고 새롭게 현재 수부터 시작한다.
#
# 마지막으로 DP 배열에서 가장 큰 누적값을 출력하면 정답이다.

from sys import stdin

N = int(stdin.readline().rstrip())
DP = [0 for _ in range(N)]
sequence = list(map(int, input().split()))

DP[0] = sequence[0]

for index in range(N):
    if sequence[index] <= DP[index - 1] + sequence[index]:
        DP[index] = DP[index - 1] + sequence[index]
    else:
        DP[index] = sequence[index]

print(max(DP))