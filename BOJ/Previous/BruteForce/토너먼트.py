# 1057 : 토너먼트
#
# 배열의 크기를 반으로 줄여 나가면서, 동시에 김지민과 임한수의 위치도 2로 나눈 몫으로 갱신한다.
# 김지민과 임한수의 위치를 2로 나눈 몫이 같다면, 둘은 같은 그룹에 있는 것이므로 만난 것이다.
#
# 둘이 만나는 경우 반복문을 탈출하고 현재까지 진행된 라운드의 수를 출력한다.

import math

N, Kim, Lim = map(int, input().split())
has_meet = False
rounds = 0

while N > 0:
    rounds += 1
    N = math.ceil(N / 2)
    Kim = (Kim + 1) // 2
    Lim = (Lim + 1) // 2

    if Kim == Lim:
        has_meet = True
        break

if has_meet:
    print(rounds)
else:
    print(-1)