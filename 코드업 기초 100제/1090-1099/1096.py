# 1096 : [기초-2차원배열] 바둑판에 흰 돌 놓기

limit = int(input())
count = 0

board = []

for i in range(19):
    row = []
    for j in range(19):
        row.append(0)
    board.append(row)

while count < limit:
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1
    count += 1

for row in board:
    for item in row:
        print(item, end=" ")
    print()

