import sys
import heapq

from collections import deque

# 1차원 배열 (실패)
N = int(sys.stdin.readline().rstrip())
numbers = []

for _ in range(N):
    line = map(int, sys.stdin.readline().rstrip().split())

    for each in line:
        heapq.heappush(numbers, -each)

result = 0
for _ in range(N):
    result = heapq.heappop(numbers)
print(-result)

# 2차원 배열 (실패)
N = int(sys.stdin.readline().rstrip())
columns = [deque() for _ in range(N)]

for _ in range(N):
    line = map(int, sys.stdin.readline().rstrip().split())

    for idx, each in enumerate(line):
        columns[idx].appendleft(-each)

heapq.heapify(columns)
result = 0

for _ in range(N):
    current = heapq.heappop(columns)
    result = current.popleft()
    heapq.heappush(columns, current)

print(-result)
