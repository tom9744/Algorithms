# 14501 : 퇴사
#
# 동적 계획법을 이용해, 마지막 날부터 첫날까지 순회하면서 해당 일자에 가능한 최대 금액을 구한다.
# 최종적으로 가능한 최대 금액이 동적 계획법으로 생성한 배열 첫번째 원소가 된다.

N = int(input())

durations = [-1, ]
incomes = [-1, ]

dp = [0 for _ in range(N + 2)]

for _ in range(N):
    duration, income = map(int, input().split())
    durations.append(duration)
    incomes.append(income)

for day in range(N, 0, -1):
    if day + durations[day] > N + 1:
        dp[day] = dp[day + 1]
    else:
        dp[day] = max(dp[day + 1], incomes[day] + dp[day + durations[day]])

print(dp[1])