import collections

N, K = map(int, input().split())
graph = [0 for n in range(100001)]

queue = collections.deque()
queue.append(N)

while queue:
    now = queue.popleft()

    if now == K:
        print(graph[now])
        break

    for step in [now - 1, now + 1, now * 2]:
        if 0 <= step < 100001 and graph[step] == 0:
            graph[step] = graph[now] + 1
            queue.append(step)
