# 1078 : [기초-종합] 짝수 합 구하기

targetNumber = int(input())

sum = 0

for num in range(1, targetNumber + 1):
    if num % 2 == 0:
        sum += num

print(sum)