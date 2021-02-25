# 14501 : 퇴사
#
# 기존에 브루트포스로 풀이했던 문제를 DP로 해결하였다.

N = int(input())

schedule = []

for _ in range(N):
    duration, profit = map(int, input().split())
    schedule.append([duration, profit])

DP = [0 for _ in range(N + 1)]

for index in range(N - 1, -1, -1):
    duration, profit = schedule[index]

    if index + duration <= N:
        DP[index] = max(DP[index + 1], DP[index + duration] + profit)
    else:
        DP[index] = DP[index + 1]

print(DP[0])