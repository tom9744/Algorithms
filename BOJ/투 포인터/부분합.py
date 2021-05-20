N, M = map(int, input().split())
numbers = list(map(int, input().split()))

left = 0
right = 0

interval_sum = numbers[0]
min_length = float('inf')

while left < N:
    # 부분합이 M보다 작은 경우, right 값을 증가시킨다.
    if interval_sum < M:
        right += 1
        if right == N:
            break
        interval_sum += numbers[right]
    # 부분합이 M 이상인 경우, left 값을 증가시킨다.
    elif interval_sum >= M:
        min_length = min(min_length, right - left + 1)  # 최소 길이를 구한다.
        interval_sum -= numbers[left]
        left += 1

if min_length < float('inf'):
    print(min_length)
else:
    print(0)
