# 1699: 제곱수의 합
#
# 접근 방법 자체는 크게 틀리지 않은거 같은데, PyPY3 환경에서만 통과된다

import math
from sys import maxsize

N = int(input())
DP = [maxsize for _ in range(N + 1)]

for num in range(1, N + 1):
    if num % math.sqrt(num) == 0:
        DP[num] = 1
    else:
        for index in range(1, (num // 2 + 1)):
            if DP[index] + DP[num - index] < DP[num]:
                DP[num] = DP[index] + DP[num - index]

print(DP[N])