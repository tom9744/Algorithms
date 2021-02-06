# 2798 : 블랙잭
#
# 이전에 구현 문제를 풀 때 알게 되었던 'itertools' 라이브러리의 'combinations(배열, 조합 원소 수)' 메서드를 사용하여
# 조합 가능한 모든 경우의 수를 파악하고, 그 합을 구해 배열에 저장한다.
# 오름차순 정렬한 배열을 순회하며 M보다 큰 값이 나오면 멈추고, 바로 이전의 값을 출력한다.

import itertools

N, M = map(int, input().split())
cards = list(map(int, input().split()))

possible_combinations = list(map(sum, itertools.combinations(cards, 3)))
possible_combinations.sort()

result = 0

for combination in possible_combinations:
    if combination > M:
        break
    result = combination

print(result)
