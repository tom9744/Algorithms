# 1018 : 체스판 다시 칠하기
#
# 주어진 보드에서 8x8 크기로 잘라낼 수 있는 모든 경우의 수를 탐색해본다.
# 이 때, 문제의 내용을 제대로 이해하지 못해서 시간이 더 걸렸다.
#
# 8x8 크기로 잘라낸 보드판을 다시 칠한다는 뜻은 W로 시작하는 상태였다고 하더라도, B로 시작하도록 바꿀 수 있다는 것이다.
# 따라서, 8x8 크기에 대해 W로 시작하는 경우 B로 시작하는 경우 두 경우 모두에 대해 몇개의 칸을 바꿔야 하는지 계산한다.
# 이후 두 값 중 작은 값을 누적 카운트 배열에 저장했다가, 마지막으로 그 중 가장 작은 값을 출력한다.


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))

counts = []

for x in range(N - 7):
    for y in range(M - 7):
        case_white = 0
        case_black = 0
        for row in range(x, x + 8):
            for col in range(y, y + 8):
                if row % 2 == 0:
                    if col % 2 == 0:
                        if board[row][col] == "W":
                            case_black += 1
                        else:
                            case_white += 1
                    elif col % 2 != 0:
                        if board[row][col] == "B":
                            case_black += 1
                        else:
                            case_white += 1
                elif row % 2 != 0:
                    if col % 2 == 0:
                        if board[row][col] == "W":
                            case_white += 1
                        else:
                            case_black += 1
                    elif col % 2 != 0:
                        if board[row][col] == "B":
                            case_white += 1
                        else:
                            case_black += 1
        counts.append(min(case_black, case_white))

print(min(counts))