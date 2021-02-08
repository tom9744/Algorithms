# 2468 : 안전 영역
#
# 강우량 0부터 100까지 각각의 경우의 수에 대하여 지형의 침수 여부를 나타내는 배열을 하나 선언한다.
# 이후 DFS 탐색을 이용해 침수되지 않은 지형의 개수를 센다.
#
# 이 때, 파이썬 재귀함수 호출 횟수 제한으로 인해 RuntimeError: recursionError 가 나오는데,
# `sys.setrecursionlimit(100000)`를 통해 해결할 수 있다.
#
# 다만, 위의 오류가 나오는 경우 DFS 가 아니라 BFS 를 사용해 풀이하는 것을 고려하는 것이 좋다고 한다.

import sys
sys.setrecursionlimit(100000)


def DFS(map, i, j):
    if i < 0 or i >= len(map) or j < 0 or j >= len(map) or map[i][j] != 0:
        return

    map[i][j] = -1

    DFS(map, i + 1, j)
    DFS(map, i - 1, j)
    DFS(map, i, j + 1)
    DFS(map, i, j - 1)


N = int(input())
terrain = []

for idx in range(N):
    heights = list(map(int, input().split()))
    terrain.append(heights)

maximum = 0
precipitation = 0

while True:
    is_flooded = [[0 for _ in range(N)] for _ in range(N)]
    count = 0

    for x in range(N):
        for y in range(N):
            if terrain[x][y] <= precipitation:
                is_flooded[x][y] = 1

    for i in range(N):
        for j in range(N):
            if is_flooded[i][j] == 0:
                DFS(is_flooded, i, j)
                count += 1

    if maximum < count:
        maximum = count
    if precipitation == 100:
        break

    precipitation += 1

print(maximum)
