# 15662: 톱니바퀴 2
#
# 회전 이전에 톱니바퀴들의 정렬 상태에 따라 회전 여부와 방향을 결정해야 한다.
# 따라서, rotations 라는 배열을 선언해 각 톱티바퀴에 대한 회전 여부와 방향을 검토하며 기록한다.
#
# 이후, rotations 배열에 기록된 내용을 토대로 톱니바퀴 회전을 시작한다.
#
# 각 톱니바퀴의 회전은 배열의 Shift 연산과 비슷한데, 따라서 Deque 라이브러리를 사용해 구현한다.
#
# 마지막으로 12시 방향의 극 (각 톱니바퀴 배열의 첫번째 원소)이 1인 것의 수를 출력한다.

from sys import stdin
from collections import deque

T = int(stdin.readline().rstrip())
wheels = [[], ]

for _ in range(T):
    wheels.append(deque(list(map(int, stdin.readline().rstrip()))))

K = int(stdin.readline().rstrip())

for _ in range(K):
    wheelNumber, direction = map(int, stdin.readline().rstrip().split())
    rotations = [0 for _ in range(T + 1)]

    rotations[wheelNumber] = direction

    for idx in range(wheelNumber, 1, -1):
        left, right = wheels[idx - 1], wheels[idx]

        if left[2] != right[6]:
            rotations[idx - 1] = -rotations[idx]
        else:
            break

    for idx in range(wheelNumber, T):
        left, right = wheels[idx], wheels[idx + 1]

        if left[2] != right[6]:
            rotations[idx + 1] = -rotations[idx]
        else:
            break

    for idx in range(1, T + 1):
        if rotations[idx] == 1:
            temp = wheels[idx].pop()
            wheels[idx].appendleft(temp)
        elif rotations[idx] == -1:
            temp = wheels[idx].popleft()
            wheels[idx].append(temp)
        else:
            continue

count = 0
for idx in range(1, T + 1):
    if wheels[idx][0] == 1:
        count += 1
print(count)
