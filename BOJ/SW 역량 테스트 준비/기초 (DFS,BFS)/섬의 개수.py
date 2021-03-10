# 4963: 섬의 개수
#
# 이전에 BFS 탐색 알고리즘과 visited[] 배열을 이용해 풀이했던 문제에 비해
# 메모리는 비슷하게 사용했지만 코드의 길이는 절반, 수행시간은 1644ms -> 93ms 로 줄었다.
#
# 수행시간이 비약적으로 줄어든 것은 `if [now_x, now_y] not in visited:` 구문이 없어져서 그런것 같다.
#
# not in 구문의 수행시간은 O(N)인 것으로 알고 있는데,
# 이번에는 주어진 그래프 자체에 -1 값을 넣는 방법으로 방문처리를 했다.

from sys import stdin

dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [-1, 1, 0, 1, -1, 0, 1, -1]


def DFS(graph, start):
    stack = [start, ]

    while stack:
        curr = stack.pop()

        for idx in range(8):
            nx = curr[0] + dx[idx]
            ny = curr[1] + dy[idx]

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = -1
                stack.append((nx, ny))


while True:
    w, h = map(int, stdin.readline().rstrip().split())

    if w == 0 and h == 0:
        break

    landscape = [list(map(int, stdin.readline().rstrip().split())) for _ in range(h)]
    count = 0

    for row in range(h):
        for col in range(w):
            if landscape[row][col] == 1:
                landscape[row][col] = -1  # 진입 노드 방문처리
                DFS(landscape, (row, col))
                count += 1

    print(count)

# 이전에 풀었던 방법 (BFS)
#
# from sys import stdin
# from collections import deque
#
# # 동 서 남 북 / 대각선 4개 방향
# dx = [0, 0, 1, -1, 1, 1, -1, -1]
# dy = [1, -1, 0, 0, 1, -1, 1, -1]
#
#
# def BFS(maps, x, y):
#     visited = list()
#     queue = deque()
#
#     queue.append([x, y])
#
#     while len(queue) != 0:
#         now_x, now_y = queue.popleft()
#
#         if [now_x, now_y] not in visited:
#             # 방문 처리
#             visited.append([now_x, now_y])
#             maps[now_x][now_y] = -1
#
#             connected_land = []
#             # 다음 방문 가능 위치 탐색
#             for direction in range(8):
#                 next_x = now_x + dx[direction]
#                 next_y = now_y + dy[direction]
#
#                 # 지도 내에 있으면서, 아직 방문하지 않은 육지인 경우 다음 방문 배열에 추가
#                 if 0 <= next_x < len(maps) and 0 <= next_y < len(maps[0]) and maps[next_x][next_y] == 1:
#                     connected_land.append([next_x, next_y])
#
#                 # Queue 에 반영
#                 queue.extend(connected_land)
#
#
# while True:
#     width, height = map(int, stdin.readline().rstrip().split())
#     if width == 0 and height == 0:
#         break
#
#     maps = []
#     count = 0
#
#     # 지도를 그린다.
#     for _ in range(height):
#         maps.append(list(map(int, stdin.readline().rstrip().split())))
#
#     # 지도 상 모든 위치에 대해 아직 방문하지 않은 육지인 경우 BFS 실행
#     for row in range(height):
#         for col in range(width):
#             if maps[row][col] == 1:
#                 BFS(maps, row, col)
#                 count += 1
#
#     print(count)