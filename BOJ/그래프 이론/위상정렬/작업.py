import heapq

N = int(input())

graph = [[] for _ in range(N + 1)]
costs = [0 for _ in range(N + 1)]
in_degree = [0 for _ in range(N + 1)]

for idx in range(N):
    cost, cnt, *tasks = map(int, input().split())

    costs[idx + 1] = cost  # 현재 작업을 수행하는데 걸리는 비용

    # 선행 관계 반영 (N번째 일을 하기 위해, 주어진 작업을 먼저 수행해야 한다)
    for task in tasks:
        graph[task].append(idx + 1)
        in_degree[idx + 1] += 1

queue = []

for idx in range(1, N + 1):
    if in_degree[idx] == 0:
        # 바로 시작 가능한 작업들을 "비용" 기준으로 최소힙에 추가한다.
        heapq.heappush(queue, (costs[idx], idx))

total_cost = 0

# BFS 방식으로 풀면 안된다! B(10sec), C(1000sec)가 동시에 수행되고 B -> D 관계일 때
# B, C의 최대값 1000sec 값을 사용해버리면 D가 10sec 안에 끝나도 B에서 D로 넘어갈 수 없다.
while queue:
    now_cost, now_task = heapq.heappop(queue)

    for related_task in graph[now_task]:
        in_degree[related_task] -= 1

        if in_degree[related_task] == 0:
            # 선행 작업이 완료된 작업은 (현재까지 소요된 시간 + 해당 작업 소요 시간)으로 큐에 삽입한다.
            heapq.heappush(queue, (now_cost + costs[related_task], related_task))

    # 마지막에 수행되는 작업의 총 수행 시간이 정답이 된다.
    total_cost = now_cost

print(total_cost)
