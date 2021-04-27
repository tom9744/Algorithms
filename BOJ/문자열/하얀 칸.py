chess_piece = 0

for idx in range(8):
    chess_board_row = input()

    # 짝수 행은 (idx, 0)부터, 홀수 행은 (idx, 1)부터 탐색 시작
    start = 0 if idx % 2 == 0 else 1

    # 두 칸 씩 건너뛰면서 하얀 칸에 체스말이 존재하는지 확인
    for col in range(start, len(chess_board_row), 2):
        if chess_board_row[col] == "F":
            chess_piece += 1

print(chess_piece)