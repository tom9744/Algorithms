# 1987 : 알파벳
#
# DFS, BFS 만으로 접근할 경우, 첫번째 시도에서 visited 배열에 알파벳을 추가해버리기 때문에
# Queue 또는 Stack 내부에 이미 한번 처리된 알파벳이 존재하는 경우 정상적으로 작동하지 않게 된다.
#
# 따라서 '백트래킹'이라는 개념을 도입하여, 탐색을 수행하다가 유망하다고 판단되지 않는 경우
# 처음 또는 어느정도 진행했던 상태로 다시 돌아와 DFS 또는 BFS 탐색을 다시 수행하도록 해야한다.
#
# 이 문제에서는 DFS 그래프 탐색 함수를 재귀적으로 호출하는 방식으로 '백트래킹'을 수행하면서
# `answer = max(answer, count)` 코드를 통해 최대로 알파벳을 방문할 수 있는 횟수를 저장한다.
#
# 스스로 풀이하지 못하고 해답을 확인하였고, 따라서 '백트래킹'에 대한 내용을 TIL 레포지토리에 기록하기로 한다.

from sys import stdin

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y, count):
    global answer
    answer = max(answer, count)

    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < R and 0 <= ny < C and alphabets[ord(alphabet_board[nx][ny]) - 65] == 0:
            alphabets[ord(alphabet_board[nx][ny]) - 65] = 1
            DFS(nx, ny, count + 1)
            alphabets[ord(alphabet_board[nx][ny]) - 65] = 0


# R: 세로 길이, C: 가로 길이
R, C = map(int, stdin.readline().rstrip().split())
alphabet_board = [list(stdin.readline().strip()) for _ in range(R)]
alphabets = [0 for _ in range(26)]

answer = 1
alphabets[ord(alphabet_board[0][0]) - 65] = 1
DFS(0, 0, answer)

print(answer)
