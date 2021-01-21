# 4796 : 캠핑
#
# 휴가 기간 V일 동안 연속된 P일 동안 L일만 사용할 수 있다.
# 따라서 ((V // P) * L) + (V % P)만 계산하면 된다고 생각했는데,
# 4, 10, 49와 같이 (V % P)가 L보다 큰 경우 위의 식으로는 계산되지 않는다.
# 그러므로 이러한 경우 그냥 ((V // P) * L) + L로 계산하도록 조건을 하나 추가해야한다.
#

counter = 1
available = 0
results = []

while True:
    l, p, v = map(int, input().split())

    if l is 0 and p is 0 and v is 0:
        break

    if (v % p) <= l:
        available = ((v // p) * l) + (v % p)
    else:
        available = ((v // p) * l) + l

    results.append("Case %d: %d" % (counter, available))

    counter += 1

for result in results:
    print(result)