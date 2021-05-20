def check_cycle():
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        root_a = find_parent(parent, a)
        root_b = find_parent(parent, b)

        if root_a < root_b:
            parent[root_b] = parent[root_a]
        else:
            parent[root_a] = parent[root_b]

    v, e = map(int, input().split())
    parent_table = [n for n in range(v + 1)]

    cycle = False

    for _ in range(e):
        node_a, node_b = map(int, input().split())

        parent_a = find_parent(parent_table, node_a)
        parent_b = find_parent(parent_table, node_b)

        if parent_a == parent_b:
            cycle = True
            break
        else:
            union_parent(parent_table, node_a, node_b)

    return cycle


if __name__ == '__main__':
    # Input
    # 3 3
    # 1 2
    # 1 3
    # 2 3
    is_cycle = check_cycle()

    print("사이클이 존재합니다." if is_cycle else "사이클이 존재하지 않습니다.") # 사이클이 존재합니다.
