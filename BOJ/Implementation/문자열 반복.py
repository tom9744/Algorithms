# 2675 : 문자열 반복

import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    case = sys.stdin.readline().rstrip().split()
    R, string = int(case[0]), case[1]

    result = []
    chars = list(string)

    for char in chars:
        result.append(char * R)

    print("".join(result))