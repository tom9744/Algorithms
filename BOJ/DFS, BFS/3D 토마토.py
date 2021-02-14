# 7569 : 3D 토마토
#
# 처음 구현하였을 때, 모든 예제에 대해 올바른 답을 구하기는 하였지만 '시간초과'에 자꾸 걸렸다.
#
# 백준 '질의응답' 게시판에서 본 문제에서는 이미 토마토 좌표에 저장된 값을 통해 방문/미방문 여부를 나타낼 수 있으므로
# BFS 탐색을 수행하기 위해 별도의 visited 배열을 사용하지 않아도 된다고 하였다.
#
# 따라서 `if current not in visited:` 조건문을  `if boxes[current[0]][current[1]][current[2]] != 0:`로 바꾸었고,
# BFS 탐색 함수가 종료될 때 (count 값 - 1)을 반환하여 몇 일 소요되었는지 바로 알 수 있게 하였더니 통과되었다.

from sys import stdin
from collections import deque

# 동, 서, 남, 북, 상, 하
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def has_raw_tomato(boxes):
    for height in range(H):
        for row in range(N):
            for col in range(M):
                if boxes[height][row][col] == 0:
                    return True
    return False


def get_valid_coordinates(boxes, current):
    current_h, current_x, current_y = current

    next_coordinates = []

    for direction in range(6):
        next_h = current_h + dz[direction]
        next_x = current_x + dx[direction]
        next_y = current_y + dy[direction]

        if 0 <= next_h < H and 0 <= next_x < N and 0 <= next_y < M and boxes[next_h][next_x][next_y] == 0:
            next_coordinates.append([next_h, next_x, next_y])
            boxes[next_h][next_x][next_y] = boxes[current_h][current_x][current_y] + 1

    return next_coordinates


def BFS(boxes, initial_tomatoes):
    queue = deque()
    queue.extend(initial_tomatoes)
    count = 0

    while queue:
        current = queue.popleft()
        count = boxes[current[0]][current[1]][current[2]]

        if boxes[current[0]][current[1]][current[2]] != 0:
            next_tomatoes = get_valid_coordinates(boxes, current)
            queue.extend(next_tomatoes)

    return count - 1


# M: 가로, N: 세로, H: 높이
M, N, H = map(int, stdin.readline().rstrip().split())
tomato_boxes = []
ripe_tomatoes = []

# 입력을 받아 토마토 박스를 배열료 표현한다 [층, 세로, 가로]
for height in range(H):
    floor = []
    for row in range(N):
        line = list(map(int, stdin.readline().rstrip().split()))
        for col in range(M):
            if line[col] == 1:
                ripe_tomatoes.append([height, row, col])
        floor.append(line)
    tomato_boxes.append(floor)

days_taken = BFS(tomato_boxes, ripe_tomatoes)

if has_raw_tomato(tomato_boxes):
    print(-1)
else:
    print(days_taken)