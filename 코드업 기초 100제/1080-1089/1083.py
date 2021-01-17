# 1083 : [기초-종합] 3 6 9 게임의 왕이 되자!

integer = int(input())

for num in range(1, integer + 1):
    print(num if num % 3 != 0 else 'X', end=" ")
