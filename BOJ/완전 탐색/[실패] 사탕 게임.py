N = int(input())
board = [list(input()) for _ in range(N)]


def swap_and_check(origin, target):
    org_x, org_y = origin
    tar_x, tar_y = target

    # Swap
    board[org_x][org_y], board[tar_x][tar_y] = board[tar_x][tar_y], board[org_x][org_y]

    row = board[org_x]
    col = [board[elem][org_y] for elem in range(N)]

    row_count = [1 for _ in range(N)]
    col_count = [1 for _ in range(N)]

    # 같은 색으로 이루어진 가장 긴 연속 부분헹/열의 길이를 구한다.
    for idx in range(1, N):
        if row[idx] == row[idx - 1]:
            row_count[idx] = row_count[idx - 1] + 1
        if col[idx] == col[idx - 1]:
            col_count[idx] = col_count[idx - 1] + 1

    # 사탕 원상 복귀
    board[org_x][org_y], board[tar_x][tar_y] = board[tar_x][tar_y], board[org_x][org_y]

    return max(max(row_count), max(col_count))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_candies = 0

for x in range(N):
    for y in range(N):
        for n in range(4):
            nx, ny = x + dx[n], y + dy[n]

            # 범위 내에 있으며, 사탕의 색이 다른 경우
            if 0 <= nx < N and 0 <= ny < N and \
                    board[x][y] != board[nx][ny]:
                candies = swap_and_check((x, y), (nx, ny))
                max_candies = max(max_candies, candies)

print(max_candies)