import sys
input = sys.stdin.readline


def solution():
    def find_parent(node):
        if parent[node] != node:
            parent[node] = find_parent(parent[node])
        return parent[node]

    def union_parent(node_a, node_b):
        root_a = find_parent(node_a)
        root_b = find_parent(node_b)

        if root_a < root_b:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b

    v, e = map(int, input().split())
    parent = [n for n in range(1 + v)]

    edges = []
    total_cost = 0

    # 간선 정보를 입력 받는다.
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    # 비용(= 가중치)를 기준으로 오름차순 정렬한다.
    edges.sort()

    # 모든 간선에 대해 다음을 수행한다.
    for edge in edges:
        cost, a, b = edge

        # 사이클이 발생하는 경우, 무시한다.
        if find_parent(a) == find_parent(b):
            continue

        union_parent(a, b)
        total_cost += cost

    return total_cost


if __name__ == '__main__':
    result = solution()

    print(result)
