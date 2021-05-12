# 2583 : 영역 구하기
#
# DFS/BFS 그래프 탐색을 통해 공간의 개수와 각 공간의 면적을 구한다.
# 먼저 직사각형을 모두 그리고, 직사각형이 차지하는 공간은 (1)로 나타낸다.
#
# 모눈종이를 나타내는 배열의 (0, 0)부터 (N, M)까지 반복문을 수행하면서 해당 위치가 빈 공간 (0)일 경우 BFS 탐색을 수행한다.
# BFS 탐색을 통해 방문할 수 있는 모든 이어진 공간에 대해 방문 표시 (-1)를 하는 동시에, 표시할 때마다 count 를 증가시켜 면적을 구한다.
# 더 이상 방문할 공간이 없으면 반복문을 종료하고 count 값을 반환한다.
#
# 이렇게 반환된 공간의 면적 값을 배열에 저장했다가, 오름차순 정렬하여 원소 개수와 함께 출력한다.

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(paper, x, y):
    visited = list()
    queue = deque()
    count = 1

    queue.append([x, y])
    paper[x][y] = -1

    while len(queue) != 0:
        current = queue.popleft()

        if current not in visited:
            visited.append(current)

            next_nodes = []

            for direction in range(4):
                next_x = current[0] + dx[direction]
                next_y = current[1] + dy[direction]

                if 0 <= next_x < len(paper) and 0 <= next_y < len(paper[0]) and paper[next_x][next_y] == 0:
                    next_nodes.append([next_x, next_y])
                    paper[next_x][next_y] = -1
                    count += 1

            queue.extend(next_nodes)

    return count


M, N, K = map(int, input().split())
paper = [[0 for _ in range(N)] for _ in range(M)]
areas = []


for _ in range(K):
    left_bottom_x, left_bottom_y, right_top_x, right_top_y = map(int, input().split())

    for row in range(right_top_y - left_bottom_y):
        for col in range(right_top_x - left_bottom_x):
            paper[left_bottom_y + row][left_bottom_x + col] = 1

for x in range(M):
    for y in range(N):
        if paper[x][y] == 0:
            area = BFS(paper, x, y)
            areas.append(area)

areas.sort()

print(len(areas))  # 면적의 개수
for each in areas:
    print(each, end=" ")
