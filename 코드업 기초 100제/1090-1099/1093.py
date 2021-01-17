# 1093 : [기초-1차원배열] 이상한 출석 번호 부르기 (1)

calls = int(input())
sequence = input().split()
dictionary = {}

for call in sequence:
    if call in dictionary:
        dictionary[call] = dictionary[call] + 1
    else:
        dictionary[call] = 1

for number in range(1, 24):
    student = str(number)

    if student in dictionary:
        print(dictionary[student], end=' ')
    else:
        print(0, end=' ')
