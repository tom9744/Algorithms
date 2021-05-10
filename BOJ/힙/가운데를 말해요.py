import sys
import heapq

N = int(sys.stdin.readline().rstrip())
min_heap = []  # 오른쪽 부분 배열 (최소 힙)
max_heap = []  # 왼쪽 부분 배열 (최대 힙)

for idx in range(N):
    number = int(sys.stdin.readline().rstrip())

    # 최대 힙이 비어있거나, 힙의 맨 앞에 위치한 값보다 입력된 값이 작은 경우, 최대 힙에 추가한다.
    if not max_heap or number < max_heap[0][1]:
        heapq.heappush(max_heap, (-number, number))
    # 최대 힙의 맨 앞에 위치한 값보다 입력된 값이 큰 경우, 최소 힙에 추가한다.
    else:
        heapq.heappush(min_heap, number)

    # 두 힙의 균형을 맞춘다.
    if abs(len(max_heap) - len(min_heap)) > 1:
        # 최대 힙에 요소가 더 많은 경우, 최대값을 최소 힙으로 이동시킨다.
        if len(max_heap) > len(min_heap):
            _, value = heapq.heappop(max_heap)
            heapq.heappush(min_heap, value)
        # 최소 힙에 요소가 더 많은 경우, 최소값을 최대 힙으로 이동시킨다.
        else:
            value = heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-value, value))

    # 중간 값을 출력한다.
    if max_heap and min_heap:
        # 길이가 짝수인 경우, 최대 힙과 최소 힙 값 중에서 더 작은 값을 출력한다.
        if len(max_heap) + len(min_heap) % 2 == 0:
            print(max_heap[0][1])
        else:
            # 길이가 홀수이고 최소 힙의 길이가 더 길면, 최소 힙의 선두를 출력한다.
            # (ex) max [2, 1] min [3, 4, 5] total [1, 2, 3, 4, 5] => 3
            if len(max_heap) < len(min_heap):
                print(min_heap[0])
            # 길이가 홀수이고 최대 힙의 길이거 더 길면, 최대 힙의 선두를 출력한다.
            else:
                print(max_heap[0][1])
    else:
        print(max_heap[0][1])

