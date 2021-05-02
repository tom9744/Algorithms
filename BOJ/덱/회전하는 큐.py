from collections import deque

N, M = map(int, input().split(" "))
target_locations = map(int, input().split(" "))
circular_queue = deque([location for location in range(1, N + 1)])
result = 0

for target in target_locations:
    # 큐의 맨 앞에 제거 대상이 올 때까지 반복한다.
    while circular_queue and circular_queue[0] != target:
        middle = len(circular_queue) // 2
        current_location = circular_queue.index(target)

        # 목표의 인덱스가 중앙값보다 큰 경우, 데크의 오른쪽 원소를 제거한다.
        # 목표: 4, [1, 2, 3, (4), 5, 6, 7] => 왼쪽으로 이동 시 3회, 오른쪽으로 이동 시 4회
        if middle < current_location:
            rear = circular_queue.pop()
            circular_queue.appendleft(rear)
        # 목표의 인덱스가 중앙값보다 작은 경우, 데크의 왼쪽 원소를 제거한다.
        else:
            front = circular_queue.popleft()
            circular_queue.append(front)
        result += 1

    circular_queue.popleft()  # 큐의 맨 앞에 위치하게 된 목표 원소를 제거한다.

print(result)
