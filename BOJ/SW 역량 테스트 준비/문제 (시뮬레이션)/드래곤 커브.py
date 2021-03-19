# 15685: 드래곤 커브

N = int(input())
grid = [[0] * 101 for _ in range(101)]
curves = [list(map(int, input().split())) for _ in range(N)]
count = 0

for x, y, d, g in curves:
    grid[x][y] = 1  # 드래곤 커브의 시작점을 표시
    coordinates = [(x, y), ]

    # 0세대 드래곤 커브를 완성시킨다.
    if d == 0:
        coordinates.append((x + 1, y))
        grid[x + 1][y] = 1
    elif d == 1:
        coordinates.append((x, y - 1))
        grid[x][y - 1] = 1
    elif d == 2:
        coordinates.append((x - 1, y))
        grid[x - 1][y] = 1
    elif d == 3:
        coordinates.append((x, y + 1))
        grid[x][y + 1] = 1

    # 각 세대마다 다음을 수행한다.
    for _ in range(g):
        temp = coordinates.copy()  # 복사본을 생성한다.
        last = temp.pop()  # 마지막 끝 점을 꺼낸다.
        temp.reverse()  # 좌표점들의 순서를 뒤집는다.

        for origin_x, origin_y in temp:
            # 회전 기준점이 되는 마지막 점을 (0, 0)으로 만들기위해 각 좌표를 이동시킨다.
            translated_x, translated_y = origin_x - last[0], origin_y - last[1]
            # 시계방향(-90도) 회전시키고, 앞서 이동한 것을 다시 복구한다.
            new_x, new_y = -translated_y + last[0], translated_x + last[1]

            # 범위 내에 들어오는 좌표만 추가한다.
            if 0 <= new_x <= 100 and 0 <= new_y <= 100:
                coordinates.append((new_x, new_y))
                grid[new_x][new_y] = 1

# 사각형이 성립되는 경우의 수를 센다
for row in range(100):
    for col in range(100):
        square = [(row, col), (row + 1, col), (row, col + 1), (row + 1, col + 1)]
        isSquare = True

        # 4개의 좌표 중 하나라도 드래곤 커브에 포함되지 않으면 False
        for x, y in square:
            if grid[x][y] == 0:
                isSquare = False

        if isSquare:
            count += 1

print(count)
