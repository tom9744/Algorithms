# 8958 : OX 퀴즈
#
# 연속적으로 O 가 나오는 경우, combo 변수를 통해 문제를 맞출 때 얻는 점수를 증가시킨다.
# X 를 만나면, combo 변수를 0으로 초기화한다.

import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    seq = sys.stdin.readline().rstrip()
    score = 0
    combo = 0

    for quiz in seq:
        if quiz == "O":
            combo += 1
            score += combo
        else:
            combo = 0
            continue

    print(score)