# 2455 : 지능형 기차

people = 0
max_people = 0

for _ in range(4):
    leaving, boarding = map(int, input().split())

    people -= leaving

    people += boarding

    if max_people < people:
        max_people = people

print(max_people)