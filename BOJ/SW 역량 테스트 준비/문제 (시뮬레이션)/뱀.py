# 3190: 뱀
N = int(input())
K = int(input())

field = [[0] * N for _ in range(N)]  # 지도 생성

# 사과 위치를 지도에 표시
for _ in range(K):
    row, col = map(int, input().split())
    field[row - 1][col - 1] = 1

L = int(input())

turns = []
for _ in range(L):
    time, direction = input().split()
    turns.append((int(time), direction))
nextTurn = turns.pop(0)

snake = [(0, 0), ]  # 벰 위치 초기화 (큐)
field[0][0] = -1

# 동/남/서/북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0  # 뱀이 향하는 방향

timeCount = 0  # 지난 시간

while True:
    timeCount += 1

    # 다음 뱀의 위치
    nx = snake[len(snake) - 1][0] + dx[direction]
    ny = snake[len(snake) - 1][1] + dy[direction]

    if 0 <= nx < N and 0 <= ny < N:
        # 자기 몸이랑 부딪힌 경우
        if field[nx][ny] == -1:
            break
        # 사과를 발견한 경우
        elif field[nx][ny] == 1:
            field[nx][ny] = -1
            snake.append((nx, ny))
        # 사과를 발견하지 못한 경우
        elif field[nx][ny] == 0:
            field[nx][ny] = -1
            snake.append((nx, ny))
            tailX, tailY = snake.pop(0)
            field[tailX][tailY] = 0
    else:
        break

    # 필요 시 방향 전환
    if timeCount == nextTurn[0]:
        if nextTurn[1] == "D":
            direction = direction + 1 if direction + 1 < 4 else 0
        elif nextTurn[1] == "L":
            direction = direction - 1 if direction - 1 >= 0 else 3

        if turns:
            nextTurn = turns.pop(0)

print(timeCount)

