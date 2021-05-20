import sys
input = sys.stdin.readline


N, M = map(int, input().split())
parent = [n for n in range(N + 1)]  # 부모 노드를 자기자신으로 초기화


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]  # 경로 압축


def union_parent(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


edges = []
total_cost = 0
max_cost = 0

for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()  # 비용을 기준으로 간선을 오름차순 정렬한다.

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)  # 두 도시를 연결한다. (최소 비용)

        total_cost += cost
        max_cost = max(max_cost, cost)  # 사용된 간선 중 가장 비용이 높은 간선을 찾는다.

print(total_cost - max_cost)
