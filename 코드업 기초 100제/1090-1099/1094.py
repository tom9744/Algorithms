# 1094 : [기초-1차원배열] 이상한 출석 번호 부르기 (2)

calls = int(input())
sequence = input().split()

memory = []

for number in sequence:
    memory.append(int(number))

memory.reverse()

for number in memory:
    print(number, end=" ")
