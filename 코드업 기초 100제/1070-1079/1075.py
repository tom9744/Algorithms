# 1075 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기 (2)

integer = int(input())

for num in range(1, integer + 1):
    print(integer - num)
