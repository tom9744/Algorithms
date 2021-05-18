N = int(input())
M = int(input())

network = [[] for _ in range(N + 1)]

for _ in range(M):
    src, dst = map(int, input().split())
    network[src].append(dst)
    network[dst].append(src)


def DFS(start, visited=[]):
    visited.append(start)

    for node in network[start]:
        if node not in visited:
            DFS(node, visited)

    return visited


infested = DFS(1)

print(len(infested) - 1)