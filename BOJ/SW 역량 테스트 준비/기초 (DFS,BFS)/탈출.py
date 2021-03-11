# 3055: 탈출
#
# 어쩌다 보니 저번이랑 완전 똑같은 풀이로 풀었다...사람은 안변하나보다

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def fillWater(graph, nodes):
    queue = deque(nodes)
    next_nodes = []

    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == "." or graph[nx][ny] == "S":
                    graph[nx][ny] = "*"
                    next_nodes.append((nx, ny))

    return next_nodes


def moveHedgehog(graph, nodes):
    queue = deque(nodes)
    next_nodes = []

    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < R and 0 <= ny < C and timestamp[nx][ny] == -1:
                if graph[nx][ny] == "." or graph[nx][ny] == "D":
                    timestamp[nx][ny] = timestamp[x][y] + 1
                    next_nodes.append((nx, ny))

    return next_nodes


R, C = map(int, input().split())
timestamp = [[-1] * C for _ in range(R)]

beaver = 0
hedgehog = 0
waters = []
forest = []

for row in range(R):
    line = list(input())
    for col in range(C):
        if line[col] == "D":
            beaver = (row, col)
        elif line[col] == "S":
            hedgehog = (row, col)
        elif line[col] == "*":
            waters.append((row, col))
    forest.append(line)

timestamp[hedgehog[0]][hedgehog[1]] = 0
hedgehogMoves = [hedgehog, ]

while True:
    waters = fillWater(forest, waters)
    hedgehogMoves = moveHedgehog(forest, hedgehogMoves)

    if len(waters) == 0 and len(hedgehogMoves) == 0:  # 여기가 문제였다...
        break

print(timestamp[beaver[0]][beaver[1]] if timestamp[beaver[0]][beaver[1]] != -1 else "KAKTUS")
