# 4963 : 섬의 개수
#
# 매우 전형적인 DFS/BFS 탐색 문제 중 하나이다.

from sys import stdin
from collections import deque

# 동 서 남 북 / 대각선 4개 방향
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


def BFS(maps, x, y):
    visited = list()
    queue = deque()

    queue.append([x, y])

    while len(queue) != 0:
        now_x, now_y = queue.popleft()

        if [now_x, now_y] not in visited:
            # 방문 처리
            visited.append([now_x, now_y])
            maps[now_x][now_y] = -1

            connected_land = []
            # 다음 방문 가능 위치 탐색
            for direction in range(8):
                next_x = now_x + dx[direction]
                next_y = now_y + dy[direction]

                # 지도 내에 있으면서, 아직 방문하지 않은 육지인 경우 다음 방문 배열에 추가
                if 0 <= next_x < len(maps) and 0 <= next_y < len(maps[0]) and maps[next_x][next_y] == 1:
                    connected_land.append([next_x, next_y])

                # Queue 에 반영
                queue.extend(connected_land)


while True:
    width, height = map(int, stdin.readline().rstrip().split())
    if width == 0 and height == 0:
        break

    maps = []
    count = 0

    # 지도를 그린다.
    for _ in range(height):
        maps.append(list(map(int, stdin.readline().rstrip().split())))

    # 지도 상 모든 위치에 대해 아직 방문하지 않은 육지인 경우 BFS 실행
    for row in range(height):
        for col in range(width):
            if maps[row][col] == 1:
                BFS(maps, row, col)
                count += 1

    print(count)