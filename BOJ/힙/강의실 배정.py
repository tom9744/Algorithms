import heapq
import sys

N = int(sys.stdin.readline().rstrip())

classes = []
current = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    classes.append((start, end))

classes.sort()

for idx in range(N):
    if current and current[0][0] <= classes[idx][0]:
        heapq.heappop(current)  # 종료된 강의 제거
    heapq.heappush(current, (classes[idx][1], classes[idx][0]))

print(len(current))