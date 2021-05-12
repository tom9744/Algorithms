# 2606 : 바이러스
#
# BFS 그래프 탐색을 통해 감염된 컴퓨터 개수를 센 다음, 문제의 조건에 따라 -1 해주면 된다.

from collections import deque


def BFS(network):
    visited = list()
    queue = deque()

    count = 0
    queue.append(1)

    while len(queue) != 0:
        current = queue.popleft()

        if current not in visited:
            visited.append(current)

            next = []
            for index in range(len(network[current])):
                if network[current][index] == 1:
                    next.append(index)

            queue.extend(next)
            count += 1

    return count


V = int(input())
E = int(input())
connections = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
for _ in range(E):
    comA, comB = map(int, input().split())
    connections[comA][comB] = 1
    connections[comB][comA] = 1

print(BFS(connections) - 1)

