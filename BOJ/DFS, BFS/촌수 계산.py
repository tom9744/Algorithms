# 2644 : 촌수 계산
#
# BFS 탐색을 통해 시작 노드부터 시작해 목표 노드를 발견하기 까지 몇 개의 레벨을 거쳐왔는지 구하면 된다.
#
# 지도 형태가 아닌, 그래프 형태로 주어지는 문제이기 때문에 방문 여부를 저장할 배열 visited 를 별도로 선언해 주어야 한다.
# 이 배열은 전체 노드 개수만큼의 길이를 가지며, 전부 0으로 초기화되어 있다.
#
# BFS 탐색을 통해 노드들을 순회하면서 해당 노드와 연결된 노드들에 대해 검사하고, 아직 방문하지 않은 경우 Queue 에 추가한다.
# (이 때, visited 배열에 시작 노드로부터의 거리를 저장해 주어야 한다.)

from collections import deque


def BFS(relations, start, target):
    queue = deque()
    queue.append(start)
    visited[start] = 1  # [중요] 시작 노드 값을 0으로 두면 안된다.

    while len(queue) != 0:
        current_node = queue.popleft()

        # 목표 노드에 도착한 경우 종료한다.
        if current_node == target:
            break

        next_nodes = []

        for index in range(len(relations)):
            # 현재 노드와 연결된 노드 중, 아직 방문하지 않은 노드만 선택하여 다음 노드 배열에 넣는다.
            if relations[current_node][index] == 1 and visited[index] == 0:
                next_nodes.append(index)
                visited[index] = visited[current_node] + 1  # 출발 노드로부터 다음 노드까지의 거리를 저장한다.

        queue.extend(next_nodes)


N = int(input())
personA, personB = map(int, input().split())
relations = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
visited = [0 for _ in range(len(relations))]

M = int(input())
for _ in range(M):
    x, y = map(int, input().split())

    relations[x][y] = relations[y][x] = 1

BFS(relations, personA, personB)

print(visited[personB] - 1)
