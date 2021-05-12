# 7568 : 덩치

N = int(input())
people = []
ranks = []

for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))


for person in people:
    rank = 1
    for idx in range(N):
        current = people[idx]

        if person[0] < current[0] and person[1] < current[1]:
            rank += 1

    print(rank, end=" ")