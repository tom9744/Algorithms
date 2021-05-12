# 3190 : 뱀
#
# 뱀의 머리 위치를 저장하는 변수를 선언하고, 주어진 조건에 따라 머리를 이동한다.
# 이때, 0으로 초기화된 N x N 배열에 뱀의 몸통 위치를 그리기 위해 머리가 지나간 곳은 -1로 표기한다. (사과는 1)
#
# 사과를 먹지못해 꼬리를 움직여야 하는 경우를 위해, Queue 를 선언하고 여기에 현재까지의 뱀의 머리 위치를 저장한다.
# 사과를 먹지 못하는 경우가 발생하면, Queue 에서 가장 옛날의 머리 위치를 가져와 해당 위치를 -1에서 0으로 바꾼다.
#
# 만약 범위를 벗어나거나 머리가 몸통에 부딧히면 반복문을 종료한다.

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())

    board[x - 1][y - 1] = 1

L = int(input())
turnarounds = []
for _ in range(L):
    second, direction = input().split()
    turnarounds.append((int(second), direction))

turnarounds.sort(key=lambda elem: elem[0])

# 초기 상태
head = [0, 0]
tail = [0, 0]
move_history = []
direction = "R"

# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 경과시간
second = 0

while True:
    board[head[0]][head[1]] = -1
    next_x, next_y = 0, 0
    second += 1

    # 머리 먼저 이동해본다.
    if direction == "R":
        next_x = head[0] + dx[0]
        next_y = head[1] + dy[0]
    elif direction == "L":
        next_x = head[0] + dx[1]
        next_y = head[1] + dy[1]
    elif direction == "S":
        next_x = head[0] + dx[2]
        next_y = head[1] + dy[2]
    elif direction == "N":
        next_x = head[0] + dx[3]
        next_y = head[1] + dy[3]

    # 다음 머리 위치가 범위 내인 경우
    if 0 <= next_x < N and 0 <= next_y < N:
        # 현재 위치를 큐에 저장
        move_history.append(head)

        # 자기 몸과 부딪히면 게임 종료
        if board[next_x][next_y] == -1:
            break
        # 사과를 먹는 경우
        elif board[next_x][next_y] == 1:
            # 머리 이동
            head = [next_x, next_y]
        # 아무것도 없는 경우
        elif board[next_x][next_y] == 0:
            # 머리와 꼬리 이동
            head = [next_x, next_y]
            x, y = move_history.pop(0)
            board[x][y] = 0
    # 벽과 부딪히는 경우
    else:
        break

    # 경과한 시간과 회전 시간 비교
    if turnarounds and second == turnarounds[0][0]:
        t, d = turnarounds.pop(0)
        if direction == "R":
            if d == "D":
                direction = "S"
            elif d == "L":
                direction = "N"
        elif direction == "L":
            if d == "D":
                direction = "N"
            elif d == "L":
                direction = "S"
        elif direction == "S":
            if d == "D":
                direction = "L"
            elif d == "L":
                direction = "R"
        elif direction == "N":
            if d == "D":
                direction = "R"
            elif d == "L":
                direction = "L"

print(second)