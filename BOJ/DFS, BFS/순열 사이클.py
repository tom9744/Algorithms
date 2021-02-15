# 10451 : 순열 사이클
#
# 입력으로 들어오는 순열을 문제에서 주어진 조건에 따라 인접 리스트를 이용해 방향성 그래프로 나타낸다.
# 이후, 순열에 포함된 각각의 숫자에 대해 몇번째 사이클에 속하는지 표현하기 위한 배열 `cycle[번호]`를 만든다.
#
# 처음엔 모두 0으로 초기화된 cycle 배열의 원소들에 대해 숫자 1부터 시작하여 DFS 탐색을 수행한다.
# 이 때, cycle[번호]에 저장된 값이 0이어야 한다.
#
# 각각의 DFS 탐색은 방향성 그래프 상에서 연결된 숫자들을 방문하며 현재 사이클 수를 cycle[번호]에 저장한다.
# DFS 탐색을 마치고 다시 cycle[번호]를 조회하며 0이 나오는 경우 사이클 수를 증가시키고, 앞의 과정을 반복한다.
#
# 반복문이 종료된 후 cycle 배열의 최대값을 출력하면 사이클의 개수를 알 수 있다.

from sys import stdin


def DFS(num, num_of_cycle):
    stack = list()
    stack.append(num)
    cycle[num] = num_of_cycle

    while stack:
        current = stack.pop()
        next_num = graph[current]

        if cycle[next_num] == 0:
            cycle[next_num] = num_of_cycle
            stack.append(next_num)


T = int(stdin.readline().rstrip())

for _ in range(T):
    N = int(stdin.readline().rstrip())
    graph = [0 for _ in range(N + 1)]
    cycle = [0 for _ in range(N + 1)]
    permutation = list(map(int, stdin.readline().rstrip().split()))

    index = 1
    for number in permutation:
        graph[index] = number
        index += 1

    count = 1
    for index in range(1, N + 1):
        if cycle[index] == 0:
            DFS(index, count)
            count += 1

    print(max(cycle))
