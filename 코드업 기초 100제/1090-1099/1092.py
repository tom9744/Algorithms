# 1092 : [기초-종합] 함께 문제 푸는 날

x, y, z = map(int, input().split())

count = 1

while True:
    if count % x == 0 and count % y == 0 and count % z == 0:
        break
    count += 1

print(count)
