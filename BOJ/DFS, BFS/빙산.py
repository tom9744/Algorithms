# 2573 : 빙산
#
# BFS 탐색으로 섬의 개수를 수하는 알고리즘을 응용하면 풀 수 있다.
# 빙산 Queue 가 더 이상 남아있지 않을 때 까지 1. 빙하를 녹이고, 2. 빙하 구획의 개수를 센다.
# 도중의 빙하 구획의 개수가 2개 이상이 되면 반복문을 중지하며, 그렇지 않을 경우 계속한다.
#
# 빙하를 녹일 때, 주변의 물 타일의 개수를 세고 그 만큼 현재 빙하의 높이에서 빼본다.
# 결과가 0보다 큰 경우, 빙하의 높이를 갱신하고 Queue 에 다시 담는다.
# 결과가 0보다 작은 경우, 빙하가 다 녹은 것이므로 해당 위치의 값을 0으로 갱신하고 Queue 에 다시 담지 않는다.

from sys import stdin
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def meltdown(current_icebergs):
    survived_icebergs = deque()
    to_be_melted = []

    while current_icebergs:
        x, y = current_icebergs.popleft()
        water = 0

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < N and 0 <= ny < M and north_pole[nx][ny] == 0:
                water += 1

        if water == 0:
            survived_icebergs.append([x, y])
        else:
            to_be_melted.append([x, y, water])

    for x, y, melted in to_be_melted:
        melted_height = north_pole[x][y] - melted

        if melted_height > 0:
            survived_icebergs.append([x, y])
            north_pole[x][y] = melted_height
        else:
            north_pole[x][y] = 0

    return survived_icebergs


def BFS(start, count):
    queue = deque()
    queue.append(start)

    while queue:
        x, y = queue.popleft()

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < N and 0 <= ny < M and north_pole[nx][ny] != 0 and visited[nx][ny] == 0:
                visited[nx][ny] = count
                queue.append([nx, ny])


N, M = map(int, stdin.readline().strip().split())
north_pole = []
icebergs = deque()
year_passed = 0
is_separable = False

for row in range(N):
    line = list(map(int, stdin.readline().strip().split()))

    for col in range(M):
        if line[col] != 0:
            icebergs.append([row, col])

    north_pole.append(line)

while icebergs:
    visited = [[0 for _ in range(M)] for _ in range(N)]
    group_counter = 0

    icebergs = meltdown(icebergs)
    year_passed += 1

    for row in range(N):
        for col in range(M):
            if north_pole[row][col] != 0 and visited[row][col] == 0:
                group_counter += 1
                visited[row][col] = group_counter
                BFS([row, col], group_counter)

    if group_counter > 1:
        is_separable = True
        break

if is_separable:
    print(year_passed)
else:
    print(0)

