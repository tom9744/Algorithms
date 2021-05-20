def union_find():
    # x는 부모 노드를 찾고자하는 노드이다.
    def find_parent(parent, x):
        # 자기자신이 부모 노드가 아닌 경우, 상위 노드를 따라 탐색한다.
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        # 두 노드의 부모 노드를 구한다.
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        # 값이 작은 부모 노드를 가리키도록 한다.
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    v, e = map(int, input().split())
    parent_table = [n for n in range(v + 1)]  # 자기 자신으로 부모 테이블 초기화

    # Union 연산을 수행한다.
    for _ in range(e):
        node_a, node_b = map(int, input().split())
        union_parent(parent_table, node_a, node_b)

    # 각 원소가 속한 집합을 출력한다.
    for idx in range(1, v + 1):
        print(find_parent(parent_table, idx), end=" ")

    print()

    # 부모 테이블 내용을 출력한다.
    for idx in range(1, v + 1):
        print(parent_table[idx], end=" ")


if __name__ == '__main__':
    union_find()

# Input
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6
# Output
# 1 1 1 1 5 5
# 1 1 1 1 5 5
