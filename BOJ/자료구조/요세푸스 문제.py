import collections

N, K = map(int, input().split())
circular_queue = collections.deque([num for num in range(1, N + 1)])

josephus = []
cursor = K

while circular_queue:
    # K번 만큼 원형 큐를 회전시킨다.
    while cursor > 1:
        circular_queue.append(circular_queue.popleft())
        cursor -= 1

    # 원형 큐 맨 앞에 위치하게된 요소를 추출한다.
    josephus.append(str(circular_queue.popleft()))

    # 커서 위치 초기화
    cursor = K

print(f"<{', '.join(josephus)}>")
