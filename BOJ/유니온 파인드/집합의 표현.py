import sys

sys.setrecursionlimit(10**6)


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


N, M = map(int, sys.stdin.readline().rstrip().split())
parent = [num for num in range(N + 1)]

for _ in range(M):
    command, elemA, elemB = map(int, sys.stdin.readline().rstrip().split())

    # Union
    if command == 0:
        union(parent, elemA, elemB)
    # Find
    elif command == 1:
        print("YES" if find(parent, elemA) == find(parent, elemB) else "NO")
