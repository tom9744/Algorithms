import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
# 부모 노드 테이블을 자기자신으로 초기화
parent = [n for n in range(N + 1)]


# Find 연산 (경로 압축법)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# Union 연산
def union_parent(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


edges = []  # 간선 정보를 담기 위한 리스트
total = 0   # 최소 신장 트리 비용

for _ in range(M):
    src, dst, cost = map(int, input().split())
    edges.append((cost, src, dst))

edges.sort()  # 간선을 비용이 낮은 순으로 오름차순 정렬한다.

# 크루스칼 MST 알고리즘을 수행한다.
for edge in edges:
    cost, src, dst = edge

    # 사이클인 경우, 무시한다.
    if find_parent(parent, src) == find_parent(parent, dst):
        continue

    union_parent(parent, src, dst)  # 두 노드를 하나의 집합에 속하게 한다.
    total += cost

print(total)
