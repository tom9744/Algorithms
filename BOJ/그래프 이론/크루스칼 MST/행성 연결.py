def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


N = int(input())

# 자기 자신으로 부모 테이블 초기화
parent = [n for n in range(N + 1)]
# 플로우 관리 비용
costs = [list(map(int, input().split())) for _ in range(N)]

edges = []

# 간선 정보를 뽑아낸다.
for i in range(len(costs)):
    for j in range(i + 1, len(costs)):
        edges.append([costs[i][j], i, j])

edges.sort()  # 크루스칼 알고리즘 사용을 위해, 비용 기준 오름차순 정렬

min_cost = 0

for edge in edges:
    flow_cost, src, dst = edge

    # 사이클이 발생하는 경우 무시한다.
    if find(src) == find(dst):
        continue

    union(src, dst)  # 두 행성을 연결한다.
    min_cost += flow_cost

print(min_cost)
