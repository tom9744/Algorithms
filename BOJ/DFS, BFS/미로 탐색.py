# 2178 : 미로 탐색
#
# 최단 거리를 찾는 문제에서는 BFS 그래프 탐색을 사용해야 한다.
# 지도의 형태로 배열이 주어지므로, 매번 상/하/좌/우에 대해 방문 가능 여부를 점검하고,
# 방문할 수 있는 경우에 대해 자식 노드로 취급한다.
#
# 현재 위치에서 이동할 수 있는 다음 위치를 찾았다면, 해당 위치들에 대해 현재 위치의 값 + 1을 해준다.
# 이런 방식으로 BFS 가 탐색한 레벨의 깊이를 저장할 수 있다.
#
# 마지막으로 탐색이 종료되면 배열의 맨 끝 위치나, 목표한 지점의 좌표에 누적된 값을 반환하면 된다.


def BFS(maze, N, M):
    # 동, 서, 남, 북
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited = list()
    queue = list()

    queue.append([1, 1])

    while len(queue) != 0:
        x, y = queue.pop(0)

        if [x, y] not in visited:
            visited.append([x, y])

            next_moves = []
            for direction in range(4):
                next_x = x + dx[direction]
                next_y = y + dy[direction]

                if 0 < next_x <= N and 0 < next_y <= M and maze[next_x][next_y] == 1:
                    next_moves.append([next_x, next_y])
                    maze[next_x][next_y] = maze[x][y] + 1

            queue.extend(next_moves)

    return maze


N, M = map(int, input().split())
maze = [[0] * (M + 1)]

for idx in range(N):
    row = [0]
    for each in input():
        row.append(int(each))
    maze.append(row)

explored_maze = BFS(maze, N, M)

print(explored_maze[N][M])