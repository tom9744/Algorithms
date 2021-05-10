import heapq

from sys import stdin

N = int(stdin.readline().rstrip())
heap = []

for _ in range(N):
    number = int(stdin.readline().rstrip())

    if number == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        # 첫번째 키의 값이 같은 경우, 암묵적으로 두번째 키를 사용해 비교한다.
        heapq.heappush(heap, (abs(number), number))
