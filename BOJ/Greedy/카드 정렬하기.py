# 1715 : 카드 정렬하기
#
# 힙을 사용해 최소값을 낮은 시간 복잡도를 달성하며 구할 수 있다.
# 가장 작은 값 두개를 구해 더한 값을 누적하고, 그 값을 다시 힙에 추가한다.

import heapq

num_of_decks = int(input())
decks = []

for _ in range(num_of_decks):
    heapq.heappush(decks, int(input()))

if len(decks) is 0:
    print(0)
else:
    num_of_compares = 0
    while len(decks) > 1:
        num_1 = heapq.heappop(decks)
        num_2 = heapq.heappop(decks)
        num_of_compares += num_1 + num_2
        heapq.heappush(decks, num_1 + num_2)

    print(num_of_compares)