import sys

input = sys.stdin.readline

N = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(N)]
parent = [n for n in range(N)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


total = 0
edges = []

# 메모리 초과 !!
for i, coord_A in enumerate(coordinates):
    for j, coord_B in enumerate(coordinates):
        if i == j:
            continue

        xa, ya, za = coord_A
        xb, yb, zb = coord_B

        distance = min(abs(xa - xb), abs(ya - yb), abs(za - zb))

        edges.append((distance, i, j))

edges.sort()

for edge in edges:
    distance, a, b = edge

    if find_parent(parent, a) == find_parent(parent, b):
        continue

    union_parent(parent, a, b)
    total += distance

print(total)
