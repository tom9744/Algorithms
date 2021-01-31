import sys
numbers = []

for _ in range(9):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)

maximum = max(numbers)
position = numbers.index(maximum)

print(maximum)
print(position + 1)