# 1097 : [기초-2차원배열] 바둑알 십자 뒤집기

board = []

for _ in range(19):
    board.append(list(map(int, input().split())))

flip_counter = int(input())

for _ in range(flip_counter):
    x, y = map(int, input().split())

    for index in range(19):
        board[x - 1][index] = 1 if board[x - 1][index] is 0 else 0
        board[index][y - 1] = 1 if board[index][y - 1] is 0 else 0

for row in board:
    for col in row:
        print(col, end=" ")
    print()

