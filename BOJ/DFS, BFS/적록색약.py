# 10026 : 적록색약
#
# Gold 5 난이도의 문제라 걱정했지만, 생각보다 어려움 없이 풀이할 수 있었다.
# 전체적인 알고리즘의 로직은 동일한 가운데, DFS 탐색 시 "다음에 탐색할 픽셀 배열"에 추가할 대상 픽셀을 선택하는 부분만 다르다.
#
# 즉, 색약이 아닌 경우 "같은 색상을 갖는 픽셀만" 탐색 대상 배열에 넣으면 되고,
# 색약인 경우 주어진 색상이 R 또는 G일 때 "같은 색상으로 보이는 픽셀들"을 탐색 대상 배열에 넣으면 된다.
#
# 두 개의 서로다른 경우에 대해 동일한 DFS 탐색 함수를 사용하기 위해 `flag` 값을 매개변수에 추가하였고,
# 값이 0이면 색약이 아닌 경우, 값이 1이면 색약인 경우이다.
#
# 이제 전체 픽셀을 순회하면서 아직 방문하지 않은 픽셀을 만날 때 DFS 탐색 알고리즘을 호출하여
# 동일한 색상 또는 동일한 색상으로 보이는 픽셀에 대해 방문처리를 하면 된다.
#
# 최종적으로 DFS 탐색 알고리즘이 호출된 횟수가 각각의 경우에 대한 답이다.

from sys import stdin
from copy import deepcopy

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def get_identical_colors(image, current_pixel, color, flag):
    now_x, now_y = current_pixel
    next_pixels = []

    for direction in range(4):
        next_x = now_x + dx[direction]
        next_y = now_y + dy[direction]

        # 적록색약 증상이 없는 경우
        if flag == 0:
            # 범위 내의 같은 색상 픽셀만 배열에 담는다.
            if 0 <= next_x < N and 0 <= next_y < N and image[next_x][next_y] == color:
                image[next_x][next_y] = -1
                next_pixels.append([next_x, next_y])
        # 적록색약 증상이 있는 경우
        elif flag == 1:
            if 0 <= next_x < N and 0 <= next_y < N:
                # 범위 내에 있으며, 현재 픽셀이 파란색인 경우
                if color == 'B':
                    # 같은 색상(= 파란색)의 픽셀만 배열에 담는다.
                    if image[next_x][next_y] == color:
                        image[next_x][next_y] = -1
                        next_pixels.append([next_x, next_y])
                # 범위 내에 있으며, 현재 픽셀이 붉은색 또는 녹색인 경우
                else:
                    # 구분할 수 없는 색상(= 붉은색, 녹색)에 해당하는 모든 픽셀을 배열에 담는다.
                    if image[next_x][next_y] in ['R', 'G']:
                        image[next_x][next_y] = -1
                        next_pixels.append([next_x, next_y])

    # 다음에 검토할 픽셀 배열을 반환한다.
    return next_pixels


def DFS(image, x, y, flag):
    color = image[x][y]
    image[x][y] = -1  # 방문 표시
    stack = [[x, y], ]

    while stack:
        now_x, now_y = stack.pop()

        if image[now_x][now_y] not in ['R', 'G', 'B']:
            # 적록색약 증상 여부에 따라 flag 값을 다르게 설정하여 상하좌우 네 방향에 대해 같은 색상의 픽셀인지 검사한다.
            next_pixels = get_identical_colors(image, [now_x, now_y], color, flag)
            stack.extend(next_pixels)


N = int(stdin.readline())
image = []

for _ in range(N):
    line = list(stdin.readline().rstrip())
    image.append(line)

copied_image = deepcopy(image)
count_1 = 0
count_2 = 0

for row in range(N):
    for col in range(N):
        # 적록색약 증상이 없는 경우
        if image[row][col] in ['R', 'G', 'B']:
            DFS(image, row, col, 0)
            count_1 += 1
        # 적록색약 증상이 있는 경우
        if copied_image[row][col] in ['R', 'G', 'B']:
            DFS(copied_image, row, col, 1)
            count_2 += 1

print(count_1, end=" ")
print(count_2)
