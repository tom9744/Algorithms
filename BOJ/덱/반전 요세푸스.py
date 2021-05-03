# [1, 2, 3, 4, 5, 6, 7] K = 3, M = 4
# [1, 2, 4, 5, 6, 7]
# [1, 2, 4, 5, 7]
# [1, 4, 5, 7]
# [1, 4, 5] Reverse!
# [4, 5]
# [4]
# []

from collections import deque

N, K, M = map(int, input().split(" "))
people = deque([num for num in range(1, N + 1)])

direction = True  # True: 오른쪽, False: 왼쪽
count = 0

while people:
    # 제거된 사람 오른쪽의 K번째 사람을 제거한다.
    if direction:
        for _ in range(K - 1):
            temp = people.popleft()
            people.append(temp)
        removed = people.popleft()
    # 제거된 사람 왼쪽의 K번째 사람을 제거한다.
    else:
        for _ in range(K - 1):
            temp = people.pop()
            people.appendleft(temp)
        removed = people.pop()

    print(removed)  # 제거한 사람을 출력한다.
    count += 1      # 제거 횟수를 1만큼 증가시킨다.

    # 제거 횟수가 M이 되면, 방향을 전환하고 카운트를 초기화한다.
    if count == M:
        direction = not direction
        count = 0
