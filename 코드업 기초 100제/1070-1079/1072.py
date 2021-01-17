# 1072 : [기초-반복실행구조] 정수 입력받아 계속 출력하기

count = int(input())
integers = list(map(int, input().split()))

for integer in integers:
    print(integer)
