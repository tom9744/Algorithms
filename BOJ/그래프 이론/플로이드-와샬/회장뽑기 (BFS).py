import sys

from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

while True:
    src, dst = map(int, input().split())

    if src == -1 and dst == -1:
        break

    graph[src].append(dst)
    graph[dst].append(src)


# 회원의 점수는 BFS 탐색을 통해 그래프의 깊이를 구한 값이다.
# (ex) "친구의 친구"는 깊이 2짜리 그래프이다.
def BFS(start):
    visited = [False for _ in range(N + 1)]
    queue = deque()

    visited[start] = True
    queue.append(start)

    score = -1  # 그래프의 깊이

    # 현재 노드와 연결된 모든 (아직 방문하지 않은) 노드를 큐에 삽입한다.
    while queue:
        score += 1

        for _ in range(len(queue)):
            now = queue.popleft()

            for node in graph[now]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)

    # 해당 노드로부터 계산한 깊이 값을 반환한다.
    return score


scores = []
min_score = float("inf")

# 모든 노드로부터 시작하여, 그래프의 깊이를 계산한다.
for number in range(1, N + 1):
    score = BFS(number)

    scores.append(score)
    min_score = min(min_score, score)  # 깊이 최소값

candidates = [str(num + 1) for num in range(N) if scores[num] == min_score]

print(min_score, len(candidates))
print(" ".join(candidates))
