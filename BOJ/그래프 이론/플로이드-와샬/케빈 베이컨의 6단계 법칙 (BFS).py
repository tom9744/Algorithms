from collections import deque

N, M = map(int, input().split())
relationship = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    relationship[A].append(B)
    relationship[B].append(A)


def BFS(start, end):
    queue = deque()
    queue.append(start)
    visited = [start]
    depth = 0

    while queue:
        depth += 1  # 깊이 증가

        # 연결된 모든 노드를 큐에 삽입한다.
        for _ in range(len(queue)):
            person = queue.popleft()

            # 목표에 도착하면 현재까지 누적된 깊이를 반환한다.
            if person == end:
                return depth - 1

            for acquaintance in relationship[person]:
                if acquaintance not in visited:
                    visited.append(acquaintance)
                    queue.append(acquaintance)


min_bacon = float('inf')
result = 0
for i in range(1, N + 1):
    kevin_bacon_number = 0
    for j in range(1, N + 1):
        # 자기자신을 제외한 모든 사람을 알기 위해 필요한 단계의 수를 구한다.
        if i != j:
            kevin_bacon_number += BFS(i, j)

    # 가장 작은 케빈 베이컨 수를 찾는다.
    if kevin_bacon_number < min_bacon:
        min_bacon = kevin_bacon_number
        result = i

print(result)