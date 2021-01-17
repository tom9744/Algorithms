# 1088 : [기초-종합] 3의 배수는 통과?

targetNum = int(input())

for num in range(1, targetNum + 1):
    if num % 3 is 0:
        continue
    print(num, end=" ")
