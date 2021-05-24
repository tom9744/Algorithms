import math
import sys

input = sys.stdin.readline

N = int(input())
stars = [tuple(map(float, input().split())) for _ in range(N)]
parent = [n for n in range(N)]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


total = 0
edges = []

for i, starA in enumerate(stars):
    for j, starB in enumerate(stars):
        if i == j:
            continue
        xA, yA = starA  # 별 A의 x, y 좌표
        xB, yB = starB  # 별 B의 x ,y 좌표

        # 2차원 좌표평면 상 거리공식에 따라, 두 별의 거리를 계산한다.
        distance = math.sqrt((xA - xB) ** 2 + (yA - yB) ** 2)

        edges.append((distance, i, j))

edges.sort()

for edge in edges:
    distance, idxA, idxB = edge

    # 사이클을 발생시키는 간선인 경우, 무시한다.
    if find(parent, idxA) == find(parent, idxB):
        continue

    union(parent, idxA, idxB)  # 두 별을 연결한다.
    total += distance

print(total)
