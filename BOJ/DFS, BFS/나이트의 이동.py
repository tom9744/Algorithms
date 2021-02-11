# 7562 : 나이트의 이동
#
# visited 배열을 따로 선언해 사용하지 않고, 방문한 적 있는 체스판의 위치에 현재까지의 이동 횟수를 저장하는 방식으로
# 해당 격자가 이미 방문한 적이 있는지, 아니면 처음 방문하는 격자인지 판단해야 한다.
# `if 0 <= next_x < len(board) and 0 <= next_y < len(board) and board[next_x][next_y] == 0:`
#
# `if [now_x][now_y] not in visited`와 같이 사용하면 시간 초과 문제가 발생한다.
# 특히, not in 은 시간 복잡도가 꽤 높으므로, 제한 시간이 1초인 경우 사용하기 어렵다고 한다.

import sys
import collections

# 12시 방향부터 시계 방향으로 움직일 수 있는 경우의 수 8가지
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def BFS(board, now, destination):
    queue = collections.deque()
    queue.append([now[0], now[1]])

    while len(queue) != 0:
        now_x, now_y = queue.popleft()

        # 목적지 도착한 경우, 반복문 중단
        if [now_x, now_y] == destination:
            break

        # 이동할 수 있는 8가지 방향에 대해 다음을 수행한다.
        for direction in range(8):
            next_x = now_x + dx[direction]
            next_y = now_y + dy[direction]

            # 체스판 범위 내의, 아직 방문한 적 없는 위치만 Queue 에 추가한다.
            if 0 <= next_x < len(board) and 0 <= next_y < len(board) and board[next_x][next_y] == 0:
                queue.append([next_x, next_y])
                board[next_x][next_y] = board[now_x][now_y] + 1


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    size = int(sys.stdin.readline().rstrip())
    chess_board = [[0 for _ in range(size)] for _ in range(size)]
    init_location = list(map(int, sys.stdin.readline().rstrip().split()))
    goal_location = list(map(int, sys.stdin.readline().rstrip().split()))

    BFS(chess_board, init_location, goal_location)

    print(chess_board[goal_location[0]][goal_location[1]])


# 오답 코드 (시간초과)
# import sys
# import collections
#
# dx = [-2, -1, 1, 2, 2, 1, -1, -2]
# dy = [1, 2, 2, 1, -1, -2, -2, -1]
#
#
# def BFS(board, now, destination):
#     visited = list()
#     queue = collections.deque()
#
#     queue.append([now[0], now[1]])
#
#     while len(queue) != 0:
#         now_x, now_y = queue.popleft()
#
#         if [now_x, now_y] == destination:
#             break
#
#         if [now_x, now_y] not in visited:
#             visited.append([now_x, now_y])
#
#             next_positions = []
#             for direction in range(8):
#                 next_x = now_x + dx[direction]
#                 next_y = now_y + dy[direction]
#
#                 if 0 <= next_x < len(board) and 0 <= next_y < len(board) and board[next_x][next_y] == 0:
#                     now_distance = abs(now_x - destination[0]) + abs(now_y - destination[1])
#                     next_distance = abs(next_x - destination[0]) + abs(next_y - destination[1])
#
#                     if next_distance <= now_distance:
#                         next_positions.append([next_x, next_y])
#                         board[next_x][next_y] = board[now_x][now_y] + 1
#
#             queue.extend(next_positions)
#
#
# T = int(sys.stdin.readline().rstrip())
#
# for _ in range(T):
#     size = int(sys.stdin.readline().rstrip())
#     chess_board = [[0 for _ in range(size)] for _ in range(size)]
#     init_location = list(map(int, sys.stdin.readline().rstrip().split()))
#     goal_location = list(map(int, sys.stdin.readline().rstrip().split()))
#
#     BFS(chess_board, init_location, goal_location)
#
#     print(chess_board[goal_location[0]][goal_location[1]])
