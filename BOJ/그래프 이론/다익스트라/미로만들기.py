import heapq

N = int(input())
INF = float("inf")

maze = [list(map(int, input())) for _ in range(N)]
distance = [[INF] * N for _ in range(N)]


# 검은 방을 흰 방으로 바꾸는 것을 비용으로 간주하여, 다익스트라를 수행한다.
def dijkstra(src_x, src_y):
    queue = []
    heapq.heappush(queue, (0, src_x, src_y))
    distance[src_x][src_y] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        cost, x, y = heapq.heappop(queue)

        # 이미 최소 비용으로 결정된 경우 무시한다.
        if distance[x][y] < cost:
            continue

        # 네 방향에 대해 검사해본다.
        for n in range(4):
            nx, ny = x + dx[n], y + dy[n]

            if 0 <= nx < N and 0 <= ny < N:
                # 검은 방
                if maze[nx][ny] == 0:
                    new_cost = cost + 1  # 검은 방 -> 흰 방 (비용 증가)

                    # 기존 비용보다 더 저렴한 경우, 우선순위 큐에 추가
                    if new_cost < distance[nx][ny]:
                        distance[nx][ny] = new_cost  # 거리 테이블 갱신
                        heapq.heappush(queue, (new_cost, nx, ny))
                # 흰 방
                elif maze[nx][ny] == 1:
                    # 현재 비용이 기존 비용보다 더 저렴한 경우, 우선순위 큐에 추가
                    if cost < distance[nx][ny]:
                        distance[nx][ny] = cost  # 거리 테이블 갱신
                        heapq.heappush(queue, (cost, nx, ny))


dijkstra(0, 0)
print(distance[-1][-1])
