# 10971: 외판원 순회 2
#
# DFS 탐색으로 '백 트래킹'을 수행해 풀이해야 하는 문제다.
#
# DFS 재귀 호출의 종료 조건에 W[current][start] != 0를 빼먹어서 계속 틀렸다.
#
# 마지막 방문 지점에서 시작 지점으로 가는 길이 없을 수도 있으므로, 꼭 추가해 주어야 한다.


import sys


def DFS(start, current, traveled_distance, accumulator):
    global min_cost

    if traveled_distance == N - 1 and W[current][start] != 0:
        min_cost = min(min_cost, accumulator + W[current][start])
        return

    for index in range(N):
        cost = W[current][index]

        if cost != 0 and visited[index] != 1:
            visited[index] = 1
            DFS(start, index, traveled_distance + 1, accumulator + cost)
            visited[index] = 0


N = int(input())
W = []
min_cost = sys.maxsize

for _ in range(N):
    W.append(list(map(int, input().split())))

for node in range(N):
    visited = [0 for _ in range(N)]
    visited[node] = 1
    DFS(node, node, 0, 0)

print(min_cost)