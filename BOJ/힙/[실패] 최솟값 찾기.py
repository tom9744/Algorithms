import sys
import heapq
import collections

# 12 3
# 1 5 2 3 6 2 3 7 3 5 2 6
# 1 1 1 2 2 2 2 2 3 3 2 2
N, L = map(int, input().split())
numbers = list(map(int, input().split()))
window = collections.deque()
heap = []

for right, num in enumerate(numbers):
    left = right - L + 1

    if left <= 0:
        window.append(num)
        heapq.heappush(heap, num)
    else:
        prev = window.popleft()
        window.append(num)

        # 새로 윈도우 들어온 값이 현재 윈도우 최소값보다 작은 경우
        if heap[0] > num:
            heapq.heappush(heap, num)
        # 새로 윈도우에 들어온 값이 현재 윈도우 최소값보다 크고, 최소값이 윈도우를 벗어난 경우
        elif heap[0] <= num and heap[0] == prev:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

    print(heap[0], end=" ")