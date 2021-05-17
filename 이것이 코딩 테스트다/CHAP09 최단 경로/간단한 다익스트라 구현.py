import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())    # 노드의 개수와 간선의 개수
start = int(input())                # 시작 노드 번호
graph = [[] for i in range(N + 1)]  # 연결 리스트로 그래프 표현
visited = [False] * (N + 1)         # 방문 체크를 위한 리스트
distance_table = [INF] * (N + 1)    # [중요] 최단 거리 테이블을 모두 무한으로 초기화

# 그래프 구성 요소를 입력 받는다.
for _ in range(M):
    src, dest, weight = map(int, input().split())
    graph[src].append((dest, weight))


# 방문하지 않은 노드 중에서, 최단 거리가 가장 짧은 노드의 번호를 반환한다.
def get_cheapest_node():
    min_value = INF
    index = 0
    for i in range(1, N + 1):
        if min_value > distance_table[i] and not visited[i]:
            min_value = distance_table[i]
            index = i
    return index


def dijkstra(start_node):
    # 시작 노드에 대해 초기화
    distance_table[start_node] = 0
    visited[start_node] = True
    for node, distance in graph[start_node]:
        distance_table[node] = distance

    # 시작 노드를 제외한 전체 N - 1개의 노드에 대해 반복
    for i in range(N - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내 방문 처리
        cheapest = get_cheapest_node()
        visited[cheapest] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for node, distance in graph[cheapest]:
            new_distance = distance_table[cheapest] + distance

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, 최단 거리 테이블 갱신
            if new_distance < distance_table[node]:
                distance_table[node] = new_distance


dijkstra(start)

# 출발 노드에서 다른 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, N + 1):
    print(distance_table[i], end=" ")

# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
# result: 0 2 3 1 2 4
