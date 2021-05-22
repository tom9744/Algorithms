import heapq

M, N = map(int, input().split())
INF = float("inf")

maze = [list(map(int, input())) for _ in range(N)]  # 2차원 배열로 나타낸 그래프
cost = [[INF] * M for _ in range(N)]                  # 최소 비용 테이블

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dijkstra_array(src_x, src_y):
    queue = []
    # 우선순위 큐에 시작 정점을 삽입하고, 비용 테이블 초기화
    heapq.heappush(queue, (0, src_x, src_y))
    cost[src_x][src_y] = 0

    while queue:
        now_cost, x, y = heapq.heappop(queue)

        if cost[x][y] < now_cost:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 다음 위치가 빈 방인 경우, 비용을 증가시키지 않는다.
                if maze[nx][ny] == 0:
                    # 현재 비용이 더 낮은 경우에만 우선순위 큐에 삽입한다.
                    if now_cost < cost[nx][ny]:
                        cost[nx][ny] = now_cost
                        heapq.heappush(queue, (now_cost, nx, ny))

                # 다음 위치가 벽인 경우, 비용을 1 증가시킨다.
                elif maze[nx][ny] == 1:
                    new_cost = now_cost + 1

                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        heapq.heappush(queue, (new_cost, nx, ny))


dijkstra_array(0, 0)  # (0, 0)에서 다익스트라를 수행한다.

print(cost[-1][-1])  # 계산된 (N, M) 위치의 최소 비용을 출력한다.
