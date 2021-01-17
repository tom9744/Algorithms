# 1095 : [기초-1차원배열] 이상한 출석 번호 부르기 (3)

calls = int(input())
sequence = input().split()

memory = []

for number in sequence:
    memory.append(int(number))

memory.sort()

print(memory[0])
