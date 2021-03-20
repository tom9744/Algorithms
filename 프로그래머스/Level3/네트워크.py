# 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 네트워크 (Level 3)
def DFS(graph, checks, node):
    stack = [node, ]
    checks[node] = True

    while stack:
        current_node = stack.pop()

        # 현재 노드와 연결된 노드 중, 연결되고 아직 방문하지 않은 것만 스택에 추가
        for index, isConnected in enumerate(graph[current_node]):
            if isConnected == 1 and not checks[index]:
                checks[index] = True
                stack.append(index)


def solution(n, computers):
    answer = 0
    visited = [False] * n

    # 아파트 단지 나누기, 섬의 개수 구하기와 같이 DFS 탐색을 수행하면 된다.
    for node in range(n):
        if not visited[node]:
            DFS(computers, visited, node)
            answer += 1

    return answer
