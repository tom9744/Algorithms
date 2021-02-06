# 2576 : 홀수

odds = []

for _ in range(7):
    number = int(input())

    if number % 2 == 1:
        odds.append(number)

if len(odds) == 0:
    print(-1)
else:
    odds.sort()
    print(sum(odds))
    print(odds[0])