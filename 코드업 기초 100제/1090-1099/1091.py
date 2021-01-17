# 1091 : [기초-종합] 수 나열하기 (3)

a, m, d, n = map(int, input().split())

for i in range(n):
    if i is 0:
        continue

    a = (a * m) + d

print(a)


