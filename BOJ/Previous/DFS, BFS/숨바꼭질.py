from collections import deque


def BFS(locations, N, K):
    queue = deque()
    queue.append(N)

    while len(queue) != 0:
        current = queue.popleft()

        if current == K:
            print(locations[current] - 1)

        for each in (current - 1, current + 1, current * 2):
            if 0 <= each <= 100000 and locations[each] == 0:
                locations[each] = locations[current] + 1
                queue.append(each)


N, K = map(int, input().split())
locations = [0 for _ in range(100000 + 1)]
locations[N] = 1

BFS(locations, N, K)
