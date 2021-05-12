# 3055 : 탈출
#
# 물 채우기 -> 고슴도치 이동을 하나의 'Step'으로 생각해야 한다.
# 따라서 물의 좌표를 담는 Water-Queue, 고슴도치의 위치를 담는 Hog-Queue 각각을 선언해 따로 사용해야 한다.
#
# 각각의 Queue 내부에 원소가 더 이상 남아 있지 않을 때까지 하나씩 꺼내 다음 위치를 검토하고
# 가능한 좌표는 임시 배열에 저장했다가, 마지막에 반복문이 종료될 때 Queue 에 추가 해야한다.


from sys import stdin
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def fill_water(queue):
    new_queue = deque()

    while queue:
        x, y = queue.popleft()

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < R and 0 <= ny < C:
                if field[nx][ny] == 'S' or field[nx][ny] == '.':
                    field[nx][ny] = '*'
                    new_queue.append([nx, ny])

    return new_queue


def move_hedge_hog(queue):
    new_queue = deque()

    while queue:
        x, y = queue.popleft()

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < R and 0 <= ny < C and movements[nx][ny] == 0:
                if field[nx][ny] == '.' or field[nx][ny] == 'D':
                    movements[nx][ny] = movements[x][y] + 1
                    new_queue.append([nx, ny])

    return new_queue


def BFS(hog_position, cave_position, water_positions):
    water_queue = deque()
    water_queue.extend(water_positions)

    hog_queue = deque()
    hog_queue.append(hog_position)

    movements[hog_position[0]][hog_position[1]] = 1

    while water_queue or hog_queue:
        water_queue = fill_water(water_queue)
        hog_queue = move_hedge_hog(hog_queue)


R, C = map(int, stdin.readline().rstrip().split())
movements = [[0 for _ in range(C)] for _ in range(R)]
field = []
rocks = []
waters = []
hedge_hog = [0, 0]
cave = [0, 0]

for row in range(R):
    line = list(stdin.readline().rstrip())

    for col in range(C):
        position = [row, col]
        if line[col] == 'S':
            hedge_hog = position
        elif line[col] == 'D':
            cave = position
        elif line[col] == '*':
            waters.append(position)
        elif line[col] == 'X':
            rocks.append(position)

    field.append(line)

BFS(hedge_hog, cave, waters)

if movements[cave[0]][cave[1]] == 0:
    print("KAKTUS")
else:
    print(movements[cave[0]][cave[1]] - 1)