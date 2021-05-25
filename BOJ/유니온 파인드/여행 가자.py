# 원소가 어느 집합에 속하는지 확인한다.
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


# 두 원소가 같은 집합에 속하도록 합친다.
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())
parent = [num for num in range(N + 1)]

for i in range(1, N + 1):
    line = list(map(int, input().split()))

    for j, is_connected in enumerate(line):
        # i번 도시와 j번 도시가 연결되어 있고, 사이클을 만들지 않는 경우
        if is_connected and (find(parent, i) != find(parent, j + 1)):
            union(parent, i, j + 1)  # 같은 집합에 속하도록 한다

plan = list(map(int, input().split()))  # 여행 계획
is_possible = True

for i in range(len(plan) - 1):
    src, dst = plan[i], plan[i + 1]

    # 출발지, 목적지가 같은 집합에 속하지 않으면, 불가능한 여행 계획이다
    if find(parent, src) != find(parent, dst):
        is_possible = False
        break

print("YES" if is_possible else "NO")
