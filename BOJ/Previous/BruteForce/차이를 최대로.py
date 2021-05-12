# 10819 : 차이를 최대로
#
# 데이터의 수가 그다지 많지 않으므로, permutations 라이브러리를 사용해 가능한 모든 수열에 대해
# 주어진 조건에 따라 계산을 수행한 후, 가장 큰 결과값을 출력한다.

from itertools import permutations

N = int(input())
integers = list(map(int, input().split()))
maximum = 0

for each in list(permutations(integers, N)):
    result = 0
    for idx in range(N - 1):
        result += abs(each[idx] - each[idx + 1])

    if maximum < result:
        maximum = result

print(maximum)
