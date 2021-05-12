# 1010 : 다리 놓기
#
# 조합: M개 중 N개를 순서 상관없이 뽑는 것, M! / (M - N)!
# 순열: M개 중 N개를 순서 상관있게 뽑는 것, M! / ((M - N)! * N!)
from math import factorial

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    result = factorial(M) // (factorial(M - N) * factorial(N))

    print(result)