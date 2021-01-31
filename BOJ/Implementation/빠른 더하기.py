# 15552 : 빠른 A+B
#
# input() 보다 sys.stdin.readline() 을 사용하는 것이 성능 상 유리하다.
# 하지만, 마지막 개행문자 '\n'도 입력되기 때문에 문자열을 저장하는 경우 .rstrip() 해주어야 한다.

import sys

num_of_iterations = int(input())

for _ in range(num_of_iterations):
    A, B = map(int, sys.stdin.readline().rstrip().split())

    print(A + B)

