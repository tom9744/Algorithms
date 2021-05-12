# 2156 : 포도주 시식
#
# 문제를 보고 DP 기법으로 접근해야 된다는 것은 파악할 수 있었지만,
# 포도주를 시식할 수 있는 경우의 수 세가지를 파악하는 것이 중요했는데, 이 것을 제대로 해내지 못했다.
# '계단 오르기' 문제랑 비슷한 형태라고 생각된다.

from sys import stdin

N = int(stdin.readline().rstrip())
wines = [0, ]
DP = [0, ]

for _ in range(N):
    wines.append(int(stdin.readline().rstrip()))

if N < 3:
    print(sum(wines))
else:
    # 경우의 수
    # 1. 이번 와인을 마시고, 이전의 와인도 마신 경우
    # 2. 이번 와인을 마시고, 이전의 와인은 마시지 않은 경우
    # 3. 이번 와인을 마시지 않는 경우
    DP.append(wines[1])
    DP.append(max(wines[1] + wines[2], wines[2]))
    DP.append(max(wines[1] + wines[2], wines[1] + wines[3], wines[2] + wines[3]))

    for index in range(4, N + 1):
        DP.append(max(
            DP[index - 3] + wines[index - 1] + wines[index],
            DP[index - 2] + wines[index],
            DP[index - 1]
        ))

    print(max(DP))