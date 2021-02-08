# 10974 : 순열
#
# itertools 라이브러리의 주어진 배열에서 원소의 개수 R개로 구성된 순열을 만드는 permutations 메서드를 사용한다.

from itertools import permutations

N = int(input())

for permutation in list(permutations([num for num in range(1, N + 1)], N)):
    for each in permutation:
        print(each, end=" ")
    print()