# 11725 : 트리의 부모 찾기
#
# DFS 또는 BFS 그래프 탐색 알고리즘을 사용해 루트 노드(= 1)부터 연결된 노드를 방문하면서
# 각 노드의 부모를 기억하기 위한 배열 `parents[노드 번호]`에 현재 노드의 번호를 저장한다.
#
# 다만, 그래프를 인접행렬로 나타낼 경우 메모리 초과로 오답 처리가 되기 때문에
# 인접행렬이 아닌 인접리스트를 이용해 나타내야 한다.
#
# BFS, DFS 중 무엇을 사용하던 상관 없는 것 같다.

from sys import stdin


def DFS():
    stack = list()
    stack.append(1)  # 루트 노드를 Queue 에 추가
    parents[1] = -1

    while stack:
        current_node = stack.pop()

        connected_nodes = []
        for node in nodes[current_node]:
            if parents[node] == 0:
                parents[node] = current_node
                connected_nodes.append(node)
        stack.extend(connected_nodes)


N = int(stdin.readline().rstrip())
nodes = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    nodeA, nodeB = map(int, stdin.readline().rstrip().split())
    nodes[nodeA].append(nodeB)
    nodes[nodeB].append(nodeA)

DFS()

for index in range(2, N + 1):
    print(parents[index])