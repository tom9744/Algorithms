# 1009 : 분산처리
#
# 일반적인 제곱 계산 (a ** b)를 사용하면 시간초과가 나온다.
#
# 알맞은 결과를 도출하기 위해 필요한 값은 (a ** b)를 계산했을 때 나오는 수의 마지막 자리 숫자 뿐이다.
# 따라서, 숫자 'a'의 끝자리 수만 보고 반복해 제곱했을 때 나올 수 있는 끝자리 경우의 수를 파악해야 한다.
# 예를 들어 3으로 끝나느 수의 경우, [3, 9, 7, 1]의 네가지 경우의 수가 반복된다.
#
# 이제 제곱해야 하는 횟수 'b'를 위에서 구한 배열의 길이로 나눈 나머지를 통해 (a ** b)를 계산했을 때 나오는 수의 끝자리 수를 알 수 있다.
# 3을 10번 제곱해야 하는 경우(a=3, b=10) 10을 4로 나눈 나머지는 2이고, 위의 배열의 2번째 위치에 있는 수(=9)가 끝자리 수이다.

import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    a = a % 10

    sequence = []

    if a == 0:
        result = 10
    elif a == 1 or a == 5 or a == 6:
        result = a
    elif a == 2 or a == 3 or a == 7 or a == 8 :
        # sequence = [2, 4 ,8, 6] or [8, 4, 2, 6]
        power = b % 4 if b % 4 != 0 else 4
        result = (a ** power) % 10
    elif a == 4 or a == 9:
        # sequence = [4, 6] or [9, 1]
        power = b % 2 if b % 2 != 0 else 4
        result = (a ** power) % 10

    print(result)