# 9613: GCD 합
#
# 주어진 테스트 케이스에 대해 itertools 패키지의 combination 함수를 사용해
# 두 개의 수로 만들 수 있는 쌍의 모든 조합을 구한다.
#
# 각 조합 경우의 수에 대해 GCD 계산을 위한 함수를 수행하고 결과를 누적해 출력한다.

from itertools import combinations


def get_gcd(num_1, num_2):
    remainder = 0

    if num_1 < num_2:
        temp = num_1
        num_1 = num_2
        num_2 = temp

    while num_1 % num_2 != 0:
        remainder = num_1 % num_2
        num_1 = num_2
        num_2 = remainder

    return num_2


test_cases = int(input())

for _ in range(test_cases):
    input_line = list(map(int, input().split()))
    n, numbers = input_line[0], input_line[1:]
    possible_pairs = combinations(numbers, 2)
    accumulator = 0

    for x, y in list(possible_pairs):
        accumulator += get_gcd(x, y)

    print(accumulator)
