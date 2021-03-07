# 11723: 집합
#
# 굉장히 메모리 및 시간 제한이 타이트한 문제로, PYPY3 환경에서는 메모리 초과가 난다.
#
# set()을 사용해도 되지만, 나는 들어갈 수 있는 숫자의 개수가 20개로 제한되어 있으므로
# 배열 인덱스의 위치에 1, 0을 넣는 방법으로 해당 숫자의 존재 여부를 판단하였다.
#
# 그 외에는 딱히 특별하다고 할만한 것은 없는 문제다.

from sys import stdin

M = int(stdin.readline().rstrip())
S = [0 for _ in range(21)]

for _ in range(M):
    command_line = stdin.readline().rstrip().split()
    command, value = "", 0

    if len(command_line) == 1:
        command = command_line[0]
    else:
        command = command_line[0]
        value = int(command_line[1])

    if command == "add" and S[value] != 1:
        S[value] = 1
    elif command == "remove" and S[value] != 0:
        S[value] = 0
    elif command == "check":
        print(0) if S[value] == 0 else print(1)
    elif command == "toggle":
        S[value] = 1 if S[value] == 0 else 0
    elif command == "all":
        S = [1 for _ in range(21)]
    elif command == "empty":
        S = [0 for _ in range(21)]
