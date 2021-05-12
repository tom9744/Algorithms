# 1759 : 암호 만들기
#
# 'itertools'의 'combinations'를 이용해, 정렬된 알파벳 배열에서 L 개를 선택해 만들 수 있는 조합을 구한다.
#
# 각 조합에 대해 몇 개의 모음이 포함되어 있는지 검사하고,
# 모음의 개수가 1 이상, (L - 모음의 개수)가 2 이상인 경우 출력한다.

from itertools import combinations

L, C = map(int, input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
alphabets = input().split()
alphabets.sort()

for combination in list(combinations(alphabets, L)):
    num_of_vowels = 0

    for char in combination:
        if char in vowels:
            num_of_vowels += 1

    if num_of_vowels >= 1 and L - num_of_vowels >= 2:
        print("".join(combination))