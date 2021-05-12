# 1182 : 부분수열의 합
#
# itertools 라이브러리의 combinations 메서드를 이용해 쉽게 풀 수있다.

from itertools import combinations

N, S = map(int, input().split())
integers = list(map(int, input().split()))

candidates = []

for r in range(1, N + 1):
    candidates += list(combinations(integers, r))

count = 0

for each in candidates:
    if sum(each) == S:
        count += 1

print(count)