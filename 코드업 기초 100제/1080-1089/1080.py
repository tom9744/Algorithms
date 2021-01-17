# 1080 : [기초-종합] 언제까지 더해야 할까?

limit = int(input())
acc = 0
num = 0

while acc < limit:
    num += 1
    acc += num

print(num)