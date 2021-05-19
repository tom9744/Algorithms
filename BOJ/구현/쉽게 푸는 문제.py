A, B = map(int, input().split())

# 수열을 만든다.
numbers = []
for num in range(1, 46 + 1):
    for _ in range(num):
        numbers.append(num)

print(sum(numbers[A - 1: B]))
