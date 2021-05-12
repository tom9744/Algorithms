# 2309: 일곱 난쟁이
#
# itertools.combinations 패키지를 사용해 9명 중 7명으로 만들 수 있는 조합을 구한다.
#
# 조합의 각 원소에 대해 총합이 100인지를 검사하고, 그 중 하나를 오름차순 정렬하려 출력하면 정답이다.

from itertools import combinations

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

possible_cases = []

for each in list(combinations(dwarfs, 7)):
    if sum(each) == 100:
        possible_cases.append(sorted(each))  # 오름차순 정렬

for dwarf in possible_cases[0]:
    print(dwarf)
