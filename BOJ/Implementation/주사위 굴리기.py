# 14499 : 주사위 굴리기
#
# 주사위를 길이 6의 배열로 나타내고, 동/서/남/북 4가지 방향으로 굴릴 때 배열의 원소 위치를 바꿔주는 함수를 하나 선언한다.
#
# 이후에는 K 만큼 반복문을 수행하면서 주어지는 명령에 따라 주사위를 굴리고, 이동시킨다.
# 그다지 어렵지 않은 문제인데, 조건 중 하나(주사위에 수를 복제하면, 그 칸은 0을 만든다)를 빼먹는 바람에 시간이 더 걸렸다.
# `board[next_x][next_y] = 0`를 추가해 줘야 한다.


def roll(current_status, instruction):
    next_status = current_status.copy()

    # 동쪽
    if instruction == 1:
        next_status[0] = current_status[2]
        next_status[1] = current_status[0]
        next_status[2] = current_status[5]
        next_status[5] = current_status[1]
    # 서쪽
    elif instruction == 2:
        next_status[0] = current_status[1]
        next_status[1] = current_status[5]
        next_status[2] = current_status[0]
        next_status[5] = current_status[2]
    # 북쪽
    elif instruction == 3:
        next_status[0] = current_status[3]
        next_status[3] = current_status[5]
        next_status[4] = current_status[0]
        next_status[5] = current_status[4]
    # 남쪽
    elif instruction == 4:
        next_status[0] = current_status[4]
        next_status[3] = current_status[0]
        next_status[4] = current_status[5]
        next_status[5] = current_status[3]

    return next_status


N, M, x, y, K = map(int, input().split())
board = []
instructions = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

instructions = list(map(int, input().split()))

# 동 서 북 남 이동
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
# 주사위 윗면, 동, 서, 남, 북, 아랫면
die = [0, 0, 0, 0, 0, 0]
# 현재 위치
position = (x, y)

for inst in instructions:

    # 다음 좌표
    next_x = position[0] + dx[inst - 1]
    next_y = position[1] + dy[inst - 1]

    # 지도 내부에 존재하는 경우
    if 0 <= next_x < N and 0 <= next_y < M:

        # 주사위를 굴린다
        die = roll(die, inst)

        # 이동한 새 위치에 적힌 정수
        written = board[next_x][next_y]

        # 적힌 정수가 0인 경우
        if written == 0:
            board[next_x][next_y] = die[5]
        # 적힌 정수가 자연수인 경우
        else:
            die[5] = board[next_x][next_y]
            board[next_x][next_y] = 0

        # 새 위치를 저장한다.
        position = (next_x, next_y)
    else:
        continue

    # 주사위 상단의 수
    top = die[0]

    print(top)
