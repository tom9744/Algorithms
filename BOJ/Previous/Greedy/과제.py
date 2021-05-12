# 13904 : 과제
#
# 가장 마지막날부터 첫날까지 반복하면서 당일에 수행할 수 있는 과제를 검토한다. (오늘 일자 <= 과제 마감까지 남은 시간)
# 수행할 수 있는 과제들 중, 최고점을 얻을 수 있는 과제를 수행하고 배열에서 제거한다.
# 반복이 끝나면 각 단계에서 누적한 점수 합을 출력한다.

num_of_assignments = int(input())
assignments = []
last_day = 0
total_score = 0

for _ in range(num_of_assignments):
    due, score = map(int, input().split())
    assignments.append((due, score))

    if last_day < due:
        last_day = due

assignments.sort(key=lambda elem: elem[1], reverse=True)

for day in range(last_day, 0, -1):
    temp = 0
    highest = 0

    for assignment in assignments:
        if day <= assignment[0] and highest < assignment[1]:
            highest = assignment[1]
            temp = assignment

    if temp:
        total_score += temp[1]
        assignments.remove(temp)

print(total_score)