# 13549: 숨바꼭질 3
#
# 숨바꼭질 문제와 동일한 방법으로 접근하되, 이번엔 일반적인 BFS 탐색과 달리
# 모든 경우의 수에 대해 동일한 시간이 소요되지 않는다.
#
# 앞으로 한 칸 걷기 / 뒤로 한 칸 걷기 / 2배 순간이동을 수행해 이동할 수 있는 위치에
# 현재 위치까지 소요된 시간 +1을 해주어야 하는데, 순간이동의 경우 +0을 해준다.
#
# 이미 방문처리가 된 곳에 대해서는 위의 과정을 수행하지 않아야 하므로
# 비용이 0인 순간이동을 먼저 처리해 준다.

from collections import deque


N, K = map(int, input().split())
visited = [-1 for _ in range(100001)]


def BFS(start, end):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        current = queue.popleft()

        if current == end:
            return

        # 비용이 0인 것을 먼저 수행해 주어야 한다.
        if current * 2 < 100001 and visited[current * 2] == -1:
            visited[current * 2] = visited[current]
            queue.append(current * 2)

        if current - 1 >= 0 and visited[current - 1] == -1:
            visited[current - 1] = visited[current] + 1
            queue.append(current - 1)

        if current + 1 < 100001 and visited[current + 1] == -1:
            visited[current + 1] = visited[current] + 1
            queue.append(current + 1)


BFS(N, K)

print(visited[K])
