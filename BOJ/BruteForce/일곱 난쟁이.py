# 2309 : 일곱 난쟁이
#
# 참고로 itertools.combination 을 사용하지 않고 직접 구현하면 10배 정도 느리다고 한다.

import itertools

heights = []

for _ in range(9):
    height = int(input())
    heights.append(height)

possible_combinations = list(itertools.combinations(heights, 7))

for combination in possible_combinations:
    total = sum(combination)

    if total == 100:
        for each in sorted(combination):
            print(each)
        break
