N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check_visibility(x, y, direction):
    count = 0

    nx = x + dx[direction]
    ny = y + dy[direction]

    while 0 <= nx < N and 0 <= ny < M:
        if office[nx][ny] == 6:
            break
        if str(office[nx][ny]) in "12345#":
            nx += dx[direction]
            ny += dy[direction]
            continue
        nx += dx[direction]
        ny += dy[direction]
        count += 1

    return count


def mark_visited(x, y, direction):
    nx = x + dx[direction]
    ny = y + dy[direction]

    while 0 <= nx < N and 0 <= ny < M:
        if office[nx][ny] == 6:
            break
        if str(office[nx][ny]) in "12345#":
            nx += dx[direction]
            ny += dy[direction]
            continue
        office[nx][ny] = "#"
        nx += dx[direction]
        ny += dy[direction]


for i, row in enumerate(office):
    for j, col in enumerate(row):
        if str(col) in "12345":
            # Down, Up, Right, Left
            visibilities = [
                check_visibility(i, j, 0),
                check_visibility(i, j, 1),
                check_visibility(i, j, 2),
                check_visibility(i, j, 3),
            ]

            if col == 1:
                mark_visited(i, j, visibilities.index(max(visibilities)))
            if col == 2:
                if visibilities[0] + visibilities[1] > visibilities[2] + visibilities[3]:
                    mark_visited(i, j, 0)
                    mark_visited(i, j, 1)
                else:
                    mark_visited(i, j, 2)
                    mark_visited(i, j, 3)
            if col == 3:
                candidates = [
                    visibilities[0] + visibilities[2],
                    visibilities[0] + visibilities[3],
                    visibilities[1] + visibilities[2],
                    visibilities[1] + visibilities[3]
                ]

                best_case = candidates.index(max(candidates))

                if best_case == 0:
                    mark_visited(i, j, 0)
                    mark_visited(i, j, 2)
                elif best_case == 1:
                    mark_visited(i, j, 0)
                    mark_visited(i, j, 3)
                elif best_case == 2:
                    mark_visited(i, j, 1)
                    mark_visited(i, j, 3)
                else:
                    mark_visited(i, j, 1)
                    mark_visited(i, j, 3)
            if col == 4:
                best_case = visibilities.index(min(visibilities))

                if best_case == 0:
                    mark_visited(i, j, 1)
                    mark_visited(i, j, 2)
                    mark_visited(i, j, 3)
                elif best_case == 1:
                    mark_visited(i, j, 0)
                    mark_visited(i, j, 2)
                    mark_visited(i, j, 3)
                elif best_case == 2:
                    mark_visited(i, j, 0)
                    mark_visited(i, j, 1)
                    mark_visited(i, j, 3)
                else:
                    mark_visited(i, j, 0)
                    mark_visited(i, j, 1)
                    mark_visited(i, j, 2)
            if col == 5:
                mark_visited(i, j, 0)
                mark_visited(i, j, 1)
                mark_visited(i, j, 2)
                mark_visited(i, j, 3)

result = 0

for row in office:
    result += row.count(0)
    print(row)

print(result)
