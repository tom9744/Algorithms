from collections import deque

# 노드의 개수와 간선의 개수
v, e = map(int, input().split())
# 모든 노드에 대한 진입 차수를 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 나타내는 연결 리스트(= 그래프)
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1  # 진입차수 1 증가


# 위상정렬 함수
def topology_sort():
    result = []  # 결과를 담기 위한 리스트
    queue = deque()

    # 진입차수가 0인 노드를 모두 큐에 삽입한다.
    for idx in range(1, v + 1):
        if indegree[idx] == 0:
            queue.append(idx)

    while queue:
        # 큐에서 원소 제거
        now = queue.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수 1 감소
        for node in graph[now]:
            indegree[node] -= 1

            # 새롭게 진입차수가 0이 되는 경우, 큐에 삽입한다.
            if indegree[node] == 0:
                queue.append(node)

    return result


topologically_sorted = topology_sort()

print(topologically_sorted)

# Input
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
# Output
# [1, 2, 5, 3, 6, 4, 7]
