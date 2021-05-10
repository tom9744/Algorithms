import sys
import heapq

N, M = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))

heapq.heapify(cards)  # 카드 배열을 힙으로 변경한다.

for _ in range(M):
    first = heapq.heappop(cards)   # 값이 가장 작은 카드
    second = heapq.heappop(cards)  # 값이 두번째로 작은 카드

    for _ in range(2):
        heapq.heappush(cards, first + second)  # 두 카드의 값을 합친 결과로 덮어쓴다.

print(sum(cards))