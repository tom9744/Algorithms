# 5014 : 스타트링크
#
# 평소 격자 형태의 지도, 지형 문제에서 상하좌우 4가지 방향으로 움직이는 dx, dy 배열을 사용했던 것 처럼,
# 주어진 U, D 값을 이용해 dx = [U, -D]와 같이 이동할 수 있는 경우의 수를 정의한다.
# 이번 문제는 2차원 배열이 아닌, 1차원 배열이므로 dy 배열은 필요없다.
#
# '버튼을 적어도 몇번 눌러야 하는지' 구해야 하므로, 최단 거리를 구하는 BFS 탐색을 사용한다.
# 시작점 S 부터 시작하여 Queue 에 아무 원소도 남지 않을 때까지 반복한다.
#
# 만약 도중에 Queue 에서 꺼낸 값이 G와 같다면 즉시 반복문을 종료하고 해당 위치에 저장된 값 (visited[G] - 1)을 출력한다.
# 반복문이 끝까지 수행되고도 G 위치에 도착하지 못한 경우, "use the stairs"를 출력한다.

from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [0 for _ in range(F + 1)]
dx = [U, -D]

queue = deque()
queue.append(S)
visited[S] = 1
is_possible = False

while queue:
    current = queue.popleft()

    if current == G:
        is_possible = True

    for direction in range(2):
        nx = current + dx[direction]

        if 0 < nx <= F and visited[nx] == 0:
            visited[nx] = visited[current] + 1
            queue.append(nx)

if is_possible:
    print(visited[G] - 1)
else:
    print("use the stairs")




