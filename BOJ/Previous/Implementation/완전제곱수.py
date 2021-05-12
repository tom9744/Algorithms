# 1977 : 완전제곱수

import math

M = int(input())
N = int(input())

perfect_square_numbers = []

for number in range(M, N + 1):
    if math.sqrt(number).is_integer():
        perfect_square_numbers.append(number)

if len(perfect_square_numbers) == 0:
    print(-1)
else:
    print(sum(perfect_square_numbers))
    print(perfect_square_numbers[0])