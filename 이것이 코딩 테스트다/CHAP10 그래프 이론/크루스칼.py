def find_parent(parent_table, node):
    if parent_table[node] != node:
        parent_table[node] = find_parent(parent_table, parent_table[node])
    return parent_table[node]


def union_parent(parent_table, x, y):
    root_x = find_parent(parent_table, x)
    root_y = find_parent(parent_table, y)

    if root_x < root_y:
        parent_table[root_y] = root_x
    else:
        parent_table[root_x] = root_y


v, e = map(int, input().split())
parent = [n for n in range(v + 1)]

edges = []
result = 0

# 간선 정보를 입력 받는다.
for _ in range(e):
    src, dst, cost = map(int, input().split())
    edges.append((cost, src, dst))

edges.sort()  # 비용에 대해 오름차순 정렬

for edge in edges:
    cost, src, dst = edge
    # 사이클이 존재하지 않는 경우에만 집합에 추가(= Union 연산 수행)한다.
    if find_parent(parent, src) != find_parent(parent, dst):
        union_parent(parent, src, dst)
        result += cost

print(result)

# Input
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25
# Output
# 159
