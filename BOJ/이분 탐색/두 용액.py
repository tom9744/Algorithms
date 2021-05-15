import sys

N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

minimum = sys.maxsize
result = ()

left, right = 0, len(liquids) - 1  # 투 포인터

while left < right:
    mixed = liquids[left] + liquids[right]

    # 혼합액의 특성값이 현재 최소값보다 작은 경우, 교체한다.
    if abs(mixed) < minimum:
        minimum = abs(mixed)
        result = (liquids[left], liquids[right])

    # 특성값이 음수인 경우, 왼쪽 포인터를 1 증가시킨다.
    if mixed < 0:
        left += 1
    # 특성값이 양수인 경우, 오른쪽 포인터를 1 감소시킨다.
    elif mixed > 0:
        right -= 1
    else:
        break

print(result[0], result[1])
