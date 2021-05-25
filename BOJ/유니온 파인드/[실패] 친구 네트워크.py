import sys
input = sys.stdin.readline


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


# 시간 초과 !!
def check_size(parent, x):
    x = find(parent, x)

    count = 0
    for key in parent.keys():
        if x == find(parent, key):
            count += 1

    return count


T = int(input())

for _ in range(T):
    F = int(input())
    parent = {}

    for _ in range(F):
        people = input().split()

        for person in people:
            if person not in parent:
                parent[person] = person

        union(parent, people[0], people[1])

        print(check_size(parent, people[0]))
