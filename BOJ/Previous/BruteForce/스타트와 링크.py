# 14889 : 스타트와 링크
#
# itertools 라이브러리를 사용해 풀이하는 문제이다.
# 1. 주어진 사람 수 N명을 두 팀으로 나누어야 하므로, 가장 먼저 combinations(people, N // 2)로 가능한 조합을 모두 찾는다.
#
# 2. 찾아낸 조합의 가장 앞쪽 조합과 가장 뒤쪽 조합을 선택하여 고르면, 가능한 팀 구성이 나온다.
#
# 3. 각 팀을 구성하는 구성원들의 능력치 합을 구하기 위해, 다시 한번 각 팀에서 2명씩 선택할 수 있는 조합을 모두 찾는다.
#
# 4. 주어진 계산식에 따라 팀의 능력치를 구하고, 두 팀의 차이가 최소가 되는 경우를 출력한다.

import itertools

N = int(input())
people = [idx for idx in range(N)]
abilities = []
scores = []

for _ in range(N):
    abilities.append(list(map(int, input().split())))

combinations = list(itertools.combinations(people, N // 2))

# N개 조합의 앞쪽 N/2개와 뒤쪽 N/2개를 역순으로 섞으면 가능한 조합이 나온다 (?)
for idx in range(len(combinations) // 2):
    teamA = combinations[idx]
    teamB = combinations[len(combinations) - idx - 1]
    teamA_score = 0
    teamB_score = 0

    # 팀 내에서 두명씩 짝을 지어 능력치를 합산한다.
    for x, y in list(itertools.combinations(teamA, 2)):
        teamA_score += abilities[x][y] + abilities[y][x]
    for x, y in list(itertools.combinations(teamB, 2)):
        teamB_score += abilities[x][y] + abilities[y][x]

    scores.append(abs(teamA_score - teamB_score))

print(min(scores))