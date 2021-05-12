# 14503 : 연구소
#
# BFS 그래프 탐색 방법과 완전 탐색 방법을 혼합하여 풀이해야 하는 문제였다.
#
# 3개의 벽을 필수적으로 추가한다고 하였으므로, 위치에 적힌 값이 0인 위치(= 빈칸)의 좌표 [x, y]를 모두 저장한 배열에 대해
# itertools.combinations 라이브러리를 이용해 3개의 빈칸을 선택할 수 있는 모든 조합을 만들어 낸다.
#
# 이후 각각의 조합에 따라 3개의 벽을 설치한 상태로 연구실 구조를 나타내는 배열을 수정한다. (deepcopy 이용)
# 다음으로 현재 바이러스가 존재하는 위치를 시작으로 BFS 그래프 탐색 함수를 호출한다.
#
# BFS 그래프 탐색 함수는 범위 내에 존재하는 모든 빈칸을 오염시키며, 해당 위치의 값을 0에서 2로 변경한다.
# 마지막으로 오염시킨 배열의 길이 (= 바이러스에 감염된 칸의 개수)를 반환한다.
#
# 모든 바이러스 초기 위치에 대해 BFS 그래프 탐색 수행을 마치면, (세로 길이 * 가로 길이)에서
# (초기 벽의 개수 + 3)과 (오염된 칸의 개수)를 뺀 값을 출력하면 정답이다.

from sys import stdin
from itertools import combinations
from collections import deque
from copy import deepcopy

# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(lab, start_point):
    start_x, start_y = start_point

    contaminated = list()   # 이미 오염된 구역
    queue = deque()         # 오염시킬 수 있는 구역

    lab[start_x][start_y] = 2
    queue.append([start_x, start_y])

    while len(queue) != 0:
        current = queue.popleft()

        if current not in contaminated:
            contaminated.append(current)

            next_targets = []

            for direction in range(4):
                next_x = current[0] + dx[direction]
                next_y = current[1] + dy[direction]

                # 연구실 범위 내에 존재하며, 그 칸의 값이 0(= 빈칸)인 경우
                if 0 <= next_x < N and 0 <= next_y < M and lab[next_x][next_y] == 0:
                    lab[next_x][next_y] = 2
                    next_targets.append([next_x, next_y])   # 오염시킬 칸 대상 배열에 넣는다.

            queue.extend(next_targets)

    return len(contaminated)    # 오염된 구역의 개수를 반환한다.


# N: 세로 길이, M: 가로 길이
N, M = map(int, stdin.readline().rstrip().split())
laboratory = []     # 연구실 구조를 나타내는 배열
empty_areas = []    # 빈칸(=0)의 좌표를 저장하는 배열
virus = []          # 바이러스(=2)의 좌표를 저장하는 배열
num_of_walls = 0    # 벽(=1)의 개수를 저장하는 변수

for row in range(N):
    line = list(map(int, stdin.readline().rstrip().split()))
    laboratory.append(line)

    for col in range(M):
        if line[col] == 0:
            empty_areas.append([row, col])
        elif line[col] == 1:
            num_of_walls += 1
        else:
            virus.append([row, col])

candidates = list(combinations(empty_areas, 3))     # 좌표 3개로 만들 수 있는 모든 조합을 생성해 배열로 만든다.
max_count = 0

# 좌표 3개로 만들 수 있는 모든 경우의 수에 대하여...
for candidate in candidates:
    copied = deepcopy(laboratory)
    num_of_contaminated = 0

    # 좌표 3개에 벽을 설치 (값을 0에서 1로 수정)
    for index in range(3):
        x, y = candidate[index]
        copied[x][y] = 1

    # 각각의 바이러스 초기 위치에 대해 BFS 함수 실행
    for each in virus:
        num_of_contaminated += BFS(copied, each)

    # 남은 빈칸(=0)의 개수가 안전 영역의 개수이다.
    safe_area = N * M - (num_of_walls + 3) - num_of_contaminated

    if max_count < safe_area:
        max_count = safe_area

print(max_count)



