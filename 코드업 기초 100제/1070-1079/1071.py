# 1071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기 (1)

integers = list(map(int, input().split()))

for integer in integers:
    if integer == 0:
        break
    print(integer)

