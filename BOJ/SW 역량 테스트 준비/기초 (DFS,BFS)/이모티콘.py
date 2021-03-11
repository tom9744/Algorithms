# 14226: 이모티콘 (스스로 X)
#
# 숨바꼭질 문제랑 접근 방법 자체는 비슷한데, 좀 더 복잡했다.
#
# 스스로 풀지 못하고 답안을 확인할 수 밖에 없었는데,
# visited 배열을 2차원 배열로 선언하는 방법을 전혀 떠올릴 수 없었다.
#
# visited[화면에 있는 이모티콘 수][클립보드에 있는 이모티콘 수]와 같이 배열을 선언해야 한다.
# 이후 BFS 탐색을 수행하면서 문제에서 주어진 세 가지 방법을 적용한다.
#
# 1. 클립보드로 복사
# 이 경우, visited[screen][screen]의 방문 여부(= 값이 -1이 아닌지)를 체크해야 한다.
# visited[screen][screen]는 "화면에 있는 이모티콘 개수를 클립보드로 복사한 경우"에 대한 소요 시간이다.
#
# 2. 클립보드에서 화면으로 복사
# visited[screen + clipboard][clipboard]의 방문 여부를 체크해야 한다.
# 추가적으로, (screen + clipboard)의 값이 1000보다 크지 않아야 한다.
# 여기서 visited[screen + clipboard][clipboard]는 "클립보드에 있는 이모티콘을 화면에 복사한 경우"에 대한 소요 시간이다.
#
# 3. 화면에서 이모티콘 한 개 삭제
# visited[screen - 1][clipboard]의 방문 여부를 체크해야 한다.
# 추가적으로, (screen - 1)의 값이 0보다 작지 않아야 한다.
# 여기서 visited[screen - 1][clipboard]는 "현재 화면에 있는 이모티콘 개수에서 1개를 뺀 경우"에 대한 소요 시간이다.

from collections import deque
from sys import maxsize


def BFS():
    queue = deque()
    queue.append((1, 0))
    visited[1][0] = 0

    while queue:
        screen, clipboard = queue.popleft()

        if visited[screen][screen] == -1:
            visited[screen][screen] = visited[screen][clipboard] + 1
            queue.append((screen, screen))

        if screen + clipboard < 1001 and visited[screen + clipboard][clipboard] == -1:
            visited[screen + clipboard][clipboard] = visited[screen][clipboard] + 1
            queue.append((screen + clipboard, clipboard))

        if screen - 1 >= 0 and visited[screen - 1][clipboard] == -1:
            visited[screen - 1][clipboard] = visited[screen][clipboard] + 1
            queue.append((screen - 1, clipboard))


S = int(input())
visited = [[-1] * 1001 for _ in range(1001)]

BFS()

result = maxsize
for index in range(1, S):
    if visited[S][index] != -1:
        result = min(result, visited[S][index])

print(result)
