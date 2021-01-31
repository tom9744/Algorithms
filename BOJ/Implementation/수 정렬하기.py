# 2750 : 수 정렬하기

import sys

N = int(sys.stdin.readline().rstrip())
numbers = []

for _ in range(N):
    number = int(sys.stdin.readline().rstrip())
    numbers.append(number)

numbers.sort()

for number in numbers:
    print(number)