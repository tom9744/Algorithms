# 1343 : 폴리오미노
#
# 연속되는 X...에 대해 XXXX를 AAAA로, XX를 BB로 바꾸고
# 문자열에 X가 아직 남아있다면 -1을, 그렇지 않다면 변환 결과를 출력한다.

board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if "X" in board:
    print(-1)
else:
    print(board)