# 1089 : [기초-종합] 수 나열하기 (1)

integers = list(map(int, input().split()))

for integer in integers:
    if integer == 0:
        break
    print(integer)

