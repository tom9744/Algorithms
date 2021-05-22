import heapq

INF = float("inf")


def dijkstra_array(graph, src_x, src_y):
    size = len(graph)
    distance = [[INF] * size for _ in range(size)]
    queue = []

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    # [주의] 시작점의 비용이 0이 아니다!
    heapq.heappush(queue, (graph[src_x][src_y], src_x, src_y))
    distance[src_x][src_y] = graph[src_x][src_y]

    while queue:
        current_dist, x, y = heapq.heappop(queue)

        if distance[x][y] < current_dist:
            continue

        for n in range(4):
            nx, ny = x + dx[n], y + dy[n]

            if 0 <= nx < size and 0 <= ny < size:
                new_dist = current_dist + graph[nx][ny]

                if new_dist < distance[nx][ny]:
                    distance[nx][ny] = new_dist
                    heapq.heappush(queue, (new_dist, nx, ny))

    return distance


if __name__ == '__main__':
    cnt = 1

    while True:
        N = int(input())

        if N == 0:
            break

        rupees = [list(map(int, input().split())) for _ in range(N)]

        min_cost_table = dijkstra_array(rupees, 0, 0)

        print(f"Problem {cnt}: {min_cost_table[-1][-1]}")

        cnt += 1
