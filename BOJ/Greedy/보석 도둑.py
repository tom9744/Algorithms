# 1202 : 보석 도둑
#
# 담을 수 있는 무게가 가장 작은 가방부터 시작하여 가장 비싼 보석을 담아야 한다.
# 따라서 보석 튜플 (무게, 가치)을 무게로 오름차순 정렬하고, 무게가 작은 가방부터 순회해보면서
# 담을 수 있는 보석 중 제일 비싼 보석을 담으면 된다.
#
# 다만, 단순 반복문을 사용하면 시간 초과가 나오기 때문에 `우선 순위 큐`를 사용해 구현해야 한다.
# heapq 에 값을 넣을 때 `-`를 붙여서 넣으면 최대값이 앞쪽으로 오도록 할 수 있다.

import heapq

n, k = map(int, input().split())
jewelries = []
bags = []
total = 0

for _ in range(n):
    weight, price = map(int, input().split())
    heapq.heappush(jewelries, (weight, price))

for _ in range(k):
    heapq.heappush(bags, int(input()))

candidates = []  # 우선순위 큐

for _ in range(k):
    max_weight = heapq.heappop(bags)

    while jewelries and max_weight >= jewelries[0][0]:
        price = heapq.heappop(jewelries)[1]
        heapq.heappush(candidates, -price)

    if candidates:
        total -= heapq.heappop(candidates)
    # 후보 보석과 보석 배열에 아무것도 없는 경우 반복문 종료
    elif not jewelries:
        break

print(total)