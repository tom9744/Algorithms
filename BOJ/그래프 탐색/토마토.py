import collections
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
graph = []
tomato = collections.deque()

for i in range(N):
    line = list(map(int, input().split()))

    for j in range(len(line)):
        if line[j] == 1:
            tomato.append((i, j))

    graph.append(line)


def BFS():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while tomato:
        # 현재 큐에 담긴 모든 토마토에 대해 BFS 탐색을 한 단계 수행한다.
        for _ in range(len(tomato)):
            x, y = tomato.popleft()

            for n in range(4):
                nx = x + dx[n]
                ny = y + dy[n]

                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y] + 1  # 시간의 경과를 표시한다.
                        tomato.append((nx, ny))          # 큐에 다음 위치를 삽입한다.


BFS()  # 토마토를 익힌다.

max_time = 0
is_possible = True

for row in graph:
    # 토마토를 전부 익힐 수 없는 경우, 플래그를 바꾸고 반복문을 종료한다.
    if row.count(0) > 0:
        is_possible = False
        break

    # 가장 오래 걸린 시간을 찾는다.
    max_time = max(max_time, max(row))

if is_possible:
    print(max_time - 1)  # 시작 시간 1을 뺀다.
else:
    print(-1)
