N, M = map(int, input().split())
rice_cakes = list(map(int, input().split()))

start, end = 0, max(rice_cakes)
result = 0
while start <= end:
    mid = (start + end) // 2

    cuts = 0
    for cake in rice_cakes:
        if cake > mid:
            cuts += cake - mid

    # 잘린 떡의 길이가 요청한 길이 M보다 크거나 같은 경우, 절단기 높이를 높혀야 한다.
    if cuts >= M:
        result = mid  # [중요] 최대한 덜 자른 경우가 정답이므로, 여기서 result 기록.
        start = mid + 1
    # 잘린 떡의 길이가 요청한 길이 M보다 부족한 경우, 절단기 높이를 줄여야 한다.
    else:
        end = mid - 1

print(result)

# 4 6
# 19 15 10 17
# result: 15
