# 1098 : [기초-2차원배열] 설탕과자 뽑기

height, width = map(int, input().split())
num_of_sticks = int(input())
board = []

# Init Array
for _ in range(height):
    row = []
    for _ in range(width):
        row.append(0)
    board.append(row)

# Arrange Sticks
for count in range(num_of_sticks):
    length, direction, x, y = map(int, input().split())

    if direction is 0:
        for tick in range(length):
            board[x - 1][y - 1 + tick] = 1
    else:
        for tick in range(length):
            board[x - 1 + tick][y - 1] = 1

# Print Result
for row in board:
    for item in row:
        print(item, end=" ")
    print()

