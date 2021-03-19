# 14503: 로봇 청소기

N, M = map(int, input().split())
row, col, direction = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

# 0: 북, 1: 동, 2: 남, 3: 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cleaned = 0

while True:
    # 청소한 적 없는 경우에만 청소
    if space[row][col] == 0:
        space[row][col] = -1
        cleaned += 1

    count = 0
    # 4가지 방향에 대해 모두 검토
    for _ in range(4):
        left = direction - 1 if direction - 1 >= 0 else 3

        left_row = row + dx[left]  # 현재 방향에서 왼쪽 row 값
        left_col = col + dy[left]  # 현재 방향에서 왼쪽 col 값

        # 왼쪽이 청소가 되지 않은 공간인 경우
        if space[left_row][left_col] == 0:
            direction = left  # 방향을 왼쪽으로 회전
            row = left_row  # 해당 위치로 이동
            col = left_col  # 해당 위치로 이동
            break
        else:
            direction = left  # 방향을 왼쪽으로 회전
            count += 1

    # 4가지 방향이 모두 청소되거나 벽인 경우
    if count == 4:
        back_row = row - dx[direction]  # 현재 방향에서 뒤쪽 row 값
        back_col = col - dy[direction]  # 현재 방향에서 뒤쪽 col 값

        # 뒤쪽이 벽이라면 바로 반복문 종료
        if space[back_row][back_col] == 1:
            break
        else:
            row = back_row  # 그렇지 않은 경우 한 칸 이동
            col = back_col  # 그렇지 않은 경우 한 칸 이동

print(cleaned)