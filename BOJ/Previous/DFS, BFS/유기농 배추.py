# 1012 : 유기농 배추
#
# 배추밭의 x, y 좌표가 뒤집혀 제공되어 약간 헷갈리는 했지만 전체적인 골자는 기본적인 그래프 탐색 문제와 같다.
#
# 지도를 Top to Bottom, Left to Right 방식으로 이동하면서 각 위치의 값이 1일 때, DFS 탐색을 수행한다.
# DFS 탐색은 지도상의 상/하/좌/우 위치에 대해 검사하며, 방문 가능한 경우 해당 위치의 값을 -1로 바꾼다.
#
# DFS 탐색이 수행된 횟수가 필요한 배추벌레 마리수이다.

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def DFS(farm, x, y):
    visited = []
    stack = []

    stack.append([x, y])

    while len(stack) != 0:
        current_x, current_y = stack.pop()

        if [current_x, current_y] not in visited:
            visited.append([current_x, current_y])
            farm[current_x][current_y] = -1

            next_moves = []
            for direction in range(4):
                next_x = current_x + dx[direction]
                next_y = current_y + dy[direction]

                if 0 <= next_x < N and 0 <= next_y < M and farm[next_x][next_y] == 1:
                    next_moves.append([next_x, next_y])

            stack.extend(next_moves)


T = int(input())

for _ in range(T):

    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    count = 0

    for _ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1

    for x in range(N):
        for y in range(M):
            if field[x][y] == 1:
                DFS(field, x, y)
                count += 1

    print(count)


