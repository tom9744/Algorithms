# 5565 : 영수증

total = int(input())
result = total

for _ in range(9):
    result -= int(input())

print(result)