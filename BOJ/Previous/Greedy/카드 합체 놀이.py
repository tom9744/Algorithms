# 15903 : 카드 합체 놀이
#
# 선택한 두 카드의 값을 더한 뒤, 그 결과를 두 카드에 덮어쓴다.
# 따라서 모든 카드 합체가 끝났을 때 모든 카드에 적힌 수의 합을 최소로 하려면,
# 두 장의 카드를 선택할 때 가장 작은 숫자의 카드 두 장을 선택해야 한다.
# 그러므로 Heap 구조를 사용해 최소값을 쉽게 얻어낼 수 있도록 하였다.

import heapq

num_of_card, merges = map(int, input().split())
cards = list(map(int, input().split()))
heap = []

for card in cards:
    heapq.heappush(heap, card)

for _ in range(merges):
    smallest = heapq.heappop(heap)
    smaller = heapq.heappop(heap)

    summary = smaller + smallest

    heapq.heappush(heap, summary)
    heapq.heappush(heap, summary)

print(sum(heap))