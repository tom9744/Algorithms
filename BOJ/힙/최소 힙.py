import heapq

from sys import stdin

N = int(stdin.readline().rstrip())
heap = []

for _ in range(N):
    number = int(stdin.readline().rstrip())

    if number > 0:
        heapq.heappush(heap, number)
    elif number == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

