# 1931 : 회의실 배정

num_of_conferences = int(input())
conference_plans = []

for _ in range(num_of_conferences):
    start_time, end_time = map(int, input().split())
    conference_plans.append((start_time, end_time))

conference_plans.sort(key=lambda element: [element[1], element[0]])

possible_conferences = []
end_time = 0

for plan in conference_plans:
    if plan[0] >= end_time:
        possible_conferences.append(plan)
        end_time = plan[1]

print(len(possible_conferences))
