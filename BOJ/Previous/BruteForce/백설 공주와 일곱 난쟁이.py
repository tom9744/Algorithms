# 3040 : 백설 공주와 일곱 난쟁이
from itertools import combinations

dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))

possible_combinations = combinations(dwarfs, 7)

for combination in possible_combinations:
    if sum(combination) == 100:
        for dwarf in combination:
            print(dwarf)