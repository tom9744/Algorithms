import sys
from itertools import combinations

input = sys.stdin.readline


# 팀의 능력치를 계산해 반환한다.
def calc_ability(team):
    result = 0

    for i in team:
        for j in team:
            result += S[i][j]

    return result


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# (N / 2)명으로 만들 수 있는 모든 팀의 조합을 구한다.
teams = list(combinations([n for n in range(N)], N // 2))

min_diff = float("inf")
# 조합을 양쪽에서 탐색하면, 같은 사람이 포함되지 않도록 두 팀을 고를 수 있다.
for idx in range(len(teams) // 2):
    teamA = teams[idx]
    teamB = teams[len(teams) - idx - 1]

    # 두 팀의 능력치 차이를 계산한다.
    diff = abs(calc_ability(teamA) - calc_ability(teamB))
    min_diff = min(min_diff, diff)

print(min_diff)
