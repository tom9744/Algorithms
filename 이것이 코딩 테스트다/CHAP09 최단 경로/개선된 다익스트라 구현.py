import heapq
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


def dijkstra(start_node):
    # 우선순위 큐
    priority_queue = []
    # 시작 노드로 가기 위한 최단 거리를 0으로 설정하여, 큐에 삽입한다.
    heapq.heappush(priority_queue, (0, start_node))
    distance_table[start_node] = 0

    while priority_queue:
        # 현재 가장 최단 거리가 짧은 노드를 꺼낸다.
        dist, now = heapq.heappop(priority_queue)

        # 현재 노드가 이미 처리된 적이 있다면, 건너 뛴다.
        if distance_table[now] < dist:
            continue

        # 현재 노드와 연결된 다른 노드를 확인
        for node, distance in graph[now]:
            new_distance = distance_table[now] + distance

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, 최단 거리 테이블 갱신
            if new_distance < distance_table[node]:
                distance_table[node] = new_distance
                # 우선순위 큐에 갱신된 거리를 반영해 삽입한다.
                heapq.heappush(priority_queue, (new_distance, node))


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