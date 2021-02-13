# 7576 토마토
#
# BFS 탐색으로 접근해야 한다는 것은 쉽게 알 수 있었지만, 초기에 주어지는 익은 토마토가 1개 이상일 때를 처리하기 좀 까다로웠다.
#
# 먼저 익은 토마토의 위치를 저장하는 Queue 를 만들고, 토마토 상태를 입력 받을 때 익은 토마토 위치를 찾아서 Queue 에 삽입한다.
#
# 익은 토마토 Queue 의 길이가 0이 될 때까지 반복하며, Queue 에서 토마토를 하나씩 빼면서 BFS 함수를 실행한다.
#
# BFS 함수는 동/서/남/북 네 방향에 대해 다음 위치를 검사하고, 정해진 범위를 벗어나지 않고 익지 않은 토마토가 있을 경우
# (방금 Queue 에서 뽑은 익은 토마토 위치에 저장되어 있는 값 + 1)으로 다음 토마토의 값을 갱신한다.
#
# 반복문이 종료되면 아직 farm 에 안익은 토마토(0)가 있는지 검사하고 있는 경우 is_success 플랙스를 False 로 바꾼다.
# 그렇지 않을 경우, (마지막에 익은 토마토 위치에 저장된 값 - 1)을 출력한다.

from collections import deque
from sys import stdin

# 동, 서, 남, 북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def BFS(farm, ripe_tomatoes, x, y):

    for direction in range(4):
        next_x = x + dx[direction]
        next_y = y + dy[direction]

        if 0 <= next_x < len(farm) and 0 <= next_y < len(farm[0]) and farm[next_x][next_y] == 0:
            farm[next_x][next_y] = farm[x][y] + 1
            ripe_tomatoes.append([next_x, next_y])


M, N = map(int, stdin.readline().rstrip().split())  # M: 가로, N: 세로
ripe_tomatoes = deque()
farm = []
is_success = True
time_taken = 0

for x in range(N):
    row = list(map(int, stdin.readline().rstrip().split()))

    for y in range(M):
        if row[y] == 1:
            ripe_tomatoes.append([x, y])

    farm.append(row)

while len(ripe_tomatoes) != 0:

    tomato = ripe_tomatoes.popleft()

    time_taken = farm[tomato[0]][tomato[1]]

    BFS(farm, ripe_tomatoes, tomato[0], tomato[1])

for row in range(N):
    for col in range(M):
        if farm[row][col] == 0:
            is_success = False

if is_success:
    print(time_taken - 1)
else:
    print(-1)
