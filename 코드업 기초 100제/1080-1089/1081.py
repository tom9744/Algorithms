# 1081 : [기초-종합] 주사위를 2개 던지면?

n, m = map(int, input().split())

for numA in range(1, n + 1):
    for numB in range(1, m + 1):
        print('{0} {1}'.format(numA, numB))