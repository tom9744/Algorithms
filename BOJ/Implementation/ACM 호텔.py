# 10250 : ACM 호텔
#
# 단순히 수식으로 풀 수 있는 문제다. 다만, N % H == 0 인 경우에 대한 예외 처리가 필요하다.

import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().rstrip().split())

    floor = N % H if N % H != 0 else H
    room = (N // H) + 1 if N % H != 0 else N // H

    print(floor * 100 + room)
