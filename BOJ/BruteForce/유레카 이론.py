# 10448 : 유레카 이론

from itertools import combinations_with_replacement

T = int(input())

triangle_numbers = []
current_triangle_number = 0
index = 0

for _ in range(T):
    target = int(input())
    is_possible = False

    while True:
        if current_triangle_number >= target:
            break
        index += 1
        current_triangle_number += index
        triangle_numbers.append(current_triangle_number)

    for each in list(combinations_with_replacement(triangle_numbers, 3)):
        if sum(each) == target:
            is_possible = True

    if is_possible:
        print(1)
    else:
        print(0)