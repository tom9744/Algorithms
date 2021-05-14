import collections

T = int(input())

for _ in range(T):
    N = int(input())
    closet = collections.defaultdict(int)

    if N == 0:
        print(0)
        continue

    for _ in range(N):
        _, kind = input().split()
        closet[kind] += 1

    # 같은 종류의 옷이 세 벌일 때, 안입는 경우를 포함해 총 4개의 경우의 수가 존재한다.
    result = 1
    for count in closet.values():
        result *= count + 1  # 안입는 경우 반영

    # 아무것도 안입는 단 하나의 경우를 제외한다.
    print(result - 1)
