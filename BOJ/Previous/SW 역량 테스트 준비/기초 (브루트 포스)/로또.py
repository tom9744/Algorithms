# 6603: 로또
#
# itertools.combination 패키지를 사용해 주어진 숫자 집합에서 6개를 골라
# 만들 수 있는 경우의 수를 모두 출력하면 된다.

from itertools import combinations

while True:
    line = list(map(int, input().split()))
    k, numbers = line[0], line[1:]

    if k == 0:
        break

    for each in list(combinations(numbers, 6)):
        for num in each:
            print(num, end=" ")
        print()

    print()
