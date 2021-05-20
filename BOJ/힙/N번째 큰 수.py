import heapq

N = int(input())
p_queue = []

for _ in range(N):
    numbers = map(int, input().split())
    for number in numbers:
        # 최소 힙에 여유공간이 존재하면, 조건없이 현재 숫자를 삽입한다.
        if len(p_queue) < N:
            heapq.heappush(p_queue, number)
        # 최소 힙의 최상단 요소의 값이 현재 숫자보다 작다면, 해당 요소를 제거하고 현재 숫자를 삽입한다.
        elif len(p_queue) >= N and p_queue[0] < number:
            heapq.heappop(p_queue)
            heapq.heappush(p_queue, number)

# 결과적으로 최소 힙에 가장 큰 N개의 숫자만 남게되며, 그중 가장 작은 값이 전체에서 N번째 큰 수이다.
print(p_queue[0])
