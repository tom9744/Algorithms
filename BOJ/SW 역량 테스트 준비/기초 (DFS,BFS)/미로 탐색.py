# 2178: 미로 탐색
#
# `if node not in visited` 조건문을 사용하지 않고
# '단지 번호 붙이기' 문제와 같이 주어진 그래프의 값을 바꾸는 방법으로
# 방문 처리를 수행했더니 수행시간이 1208ms 에서 132ms 까지 단축되었다.

from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(graph, node):
    queue = deque()
    queue.append(node)
    graph[node[0]][node[1]] = -1

    while queue:
        curr = queue.popleft()

        for idx in range(4):
            nx = curr[0] + dx[idx]
            ny = curr[1] + dy[idx]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[curr[0]][curr[1]] - 1
                queue.append((nx, ny))


BFS(maze, (0, 0))

print(abs(maze[N - 1][M - 1]))
