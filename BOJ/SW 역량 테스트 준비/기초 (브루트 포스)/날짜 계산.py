# 1476: 날짜 계산
#
# 반복문을 이용해 (e, s, m)을 (1, 1, 1)부터 시작해 규칙에 따라 증가시켜 나가면서
# 입력받은 (E, S, M)과 같아지는 경우까지 반복한다.
#
# e == E, s == S, m == M 일 때, 반복문을 수행한 횟수(= year)를 출력하면 정답이다.

E, S, M = map(int, input().split())
e, s, m = 1, 1, 1
year = 1

while True:
    if E == e and S == s and M == m:
        break

    e += 1
    s += 1
    m += 1
    year += 1

    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1

print(year)
