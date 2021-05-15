N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

low, high = 0, max(trees)

while low <= high:
    mid = (low + high) // 2

    # 시간 초과 O(N)
    # logs = 0
    # for tree in trees:
    #     if tree > mid:
    #         logs += tree - mid

    # 리스트 컴프리헨션을 통해 시간복잡도 개선
    logs = sum([tree - mid for tree in trees if tree > mid])

    if logs >= M:
        low = mid + 1
    else:
        high = mid - 1

print(high)
