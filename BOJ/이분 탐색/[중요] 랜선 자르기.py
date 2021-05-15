from sys import stdin

K, N = map(int, stdin.readline().rstrip().split())
lines = [int(stdin.readline().rstrip()) for _ in range(K)]

start, end = 1, max(lines)  # 랜선을 자를 수 있는 모든 길이

# 이분 검색을 수행한다.
while start <= end:
    mid = (start + end) // 2

    cuts = 0
    # 가지고 있는 랜선을 잘라 만들 수 있는 랜선의 개수를 구한다.
    for line in lines:
        cuts += line // mid

    # 잘린 개수가 목표치보다 많은 경우
    if cuts >= N:
        start = mid + 1
    # 잘린 개수가 목표피보다 부족한 경우
    elif cuts < N:
        end = mid - 1

print(end)