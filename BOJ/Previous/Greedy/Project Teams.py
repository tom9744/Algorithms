# 20044 : Project Teams
#
# 학생들의 코딩 역량을 담은 배열을 정렬한 뒤, (가장 역량이 낮은 학생 + 가장 역량이 높은 학생)으로 팀을 구성한다.
# 이렇게 구성된 팀의 역량을 배열에 저장하고, 마찬가지로 정렬한 뒤 최소값을 출력한다.

num_of_teams = int(input())
personal_skills = sorted(list(map(int, input().split())))
team_skills = []

for index in range(num_of_teams):
    num_of_students = len(personal_skills)
    dumb = personal_skills[index]
    smart = personal_skills[num_of_students - index - 1]
    team_skills.append(dumb + smart)

team_skills.sort()

print(team_skills[0])