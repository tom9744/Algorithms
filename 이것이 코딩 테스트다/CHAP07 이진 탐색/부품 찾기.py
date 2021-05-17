def binary_search(array, target, start, end):
    # 이진 탐색을 통해 대상 부품을 찾는다.
    while start <= end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] == target:
            return mid
    return None


N = int(input())
parts = list(map(int, input().split()))
M = int(input())
orders = list(map(int, input().split()))

parts.sort()
max_number = max(parts)

for order in orders:
    index = binary_search(parts, order, 0, N - 1)

    if index:
        print("yes", end=" ")
    else:
        print("no", end=" ")
