# 11497 : 통나무 건너뛰기
#
# 통나무 높이를 담고 있는 배열을 오름차순으로 정렬한 뒤, pop() 을 사용해 큰 값부터 하나씩 꺼낸다.
# 이러한 값을 새로운 배열의 왼쪽 끝, 오른쪽 끝에 한 번 씩 번갈아가며 삽입한다.
# 삽입할 때, 첫번째 경우를 제외하고는 바로 인접한 통나무와의 높이 차이를 계산해보며 가장 큰 값을 기억해 놓았다가 반환한다.

test_case = int(input())

for _ in range(test_case):
    num_of_log = int(input())
    logs = list(map(int, input().split()))
    logs.sort()
    alignment = []
    difficulty = 0

    for _ in range(num_of_log):
        log = logs.pop()

        if len(alignment) == 0:
            alignment.append(log)
        elif len(alignment) % 2 == 0:
            # 배열의 왼쪽 끝에 삽입
            alignment.insert(0, log)

            gap = abs(alignment[0] - alignment[1])
            if difficulty < gap:
                difficulty = gap
        else:
            # 배열의 오른쪽 끝에 삽입
            alignment.insert(len(alignment), log)

            gap = abs(alignment[len(alignment) - 1] - alignment[len(alignment) - 2])
            if difficulty < gap:
                difficulty = gap

    print(difficulty)