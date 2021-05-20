N, M = map(int, input().split())
teams = [n for n in range(N + 1)]  # 부모 테이블 초기화


def find_team(team_table, x):
    if team_table[x] != x:
        team_table[x] = find_team(team_table, team_table[x])
    return team_table[x]


def union_team(team_table, a, b):
    # a와 b가 속한 팀을 찾는다.
    team_a = find_team(team_table, a)
    team_b = find_team(team_table, b)

    # 팀번호가 낮은 팀으로 합병한다.
    if team_a < team_b:
        team_table[team_b] = team_a
    else:
        team_table[team_a] = team_b


for _ in range(M):
    command, student_a, student_b = map(int, input().split())

    # 두 학생이 같은 팀에 속하도록 팀을 합친다.
    if command == 0:
        union_team(teams, student_a, student_b)
    # 두 학생이 같은 팀에 속하는지 확인한다.
    if command == 1:
        if find_team(teams, student_a) == find_team(teams, student_b):
            print("YES")
        else:
            print("NO")

# Input
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
