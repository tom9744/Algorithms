# 10819: 차이를 최대로
#
# 주어지는 숫자의 개수가 3 ~ 8개 사이의 작은 수 이므로, itertools.permutations 패키지를 이용해
# N개의 숫자로 만들 수 있는 모든 순열을 구한다.
#
# 다음으로는 각 순열에 대해 주어진 식 (= 차이들의 총합)을 적용해 결과값을 얻어보는데,
# 이 때 가장 큰 값을 기억해 놓고 마지막에 출력하면 정답이다.

from itertools import permutations


def calculate(array, length):
    result = 0
    for index in range(length - 1):
        result += abs(array[index] - array[index + 1])

    return result


N = int(input())
numbers = list(map(int, input().split()))
maximum = 0

for each in list(permutations(numbers, N)):
    maximum = max(maximum, calculate(each, N))

print(maximum)
