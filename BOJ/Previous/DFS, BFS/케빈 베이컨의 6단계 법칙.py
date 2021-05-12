# 1389 : 케빈 베이컨의 6단계 법칙
#
# 우선 주어진 친구 관계를 표현하기 위한 무방향 그래프를 인접 리스트의 형태로 선언한다.
# 추가적으로 한 사람에서 다른 사람까지의 케빈 베이컨 거리를 저장하기 위한 배열도 선언한다.
#
# 이제 각각의 사람(= 노드)에 대해 BFS 탐색을 수행하는데, BFS 함수는 사람에 대한 케빈 베이컨 수를 반환한다.
# (알고리즘 자체는 일반적인 BFS 탐색에서 탐색 깊이를 누적하는 방식으로 수행한다.)
#
# 모든 사람에 대해 BFS 탐색을 수행해 반환받은 케빈 베이컨 수 중 최소값을 얻어낸 뒤,
# 배열에서 그 값을 가지는 가장 첫번째 원소의 위치 + 1을 출력하면 정답이다.

from sys import stdin
from collections import deque
from copy import deepcopy


def BFS(result_copy, start):
    queue = deque()
    queue.append(start)
    result_copy[start] = 1

    while queue:
        current = queue.popleft()

        next_people = []
        for person in relations[current]:
            if result_copy[person] == 0:
                result_copy[person] = result_copy[current] + 1
                next_people.append(person)
        queue.extend(next_people)

    kevin_bacon = 0

    for index in range(1, N + 1):
        kevin_bacon += result_copy[index] - 1

    return kevin_bacon


N, M = map(int, stdin.readline().rstrip().split())
relations = [[] for _ in range(N + 1)]
game_result = [0 for _ in range(N + 1)]

for _ in range(M):
    personA, personB = map(int, stdin.readline().rstrip().split())
    relations[personA].append(personB)
    relations[personB].append(personA)

best_case = 1000000
results = []

for start_person in range(1, N + 1):
    result = BFS(deepcopy(game_result), start_person)
    results.append(result)

    if result < best_case:
        best_case = result

print(results.index(best_case) + 1)
