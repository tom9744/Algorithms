import sys
import collections

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    docs = collections.deque(map(int, sys.stdin.readline().rstrip().split()))
    top_priority = max(docs)

    position = M
    count = 0
    while docs:
        # 큐 맨앞의 요소가 최고 우선순위를 가지는 경우
        if docs[0] == top_priority:
            docs.popleft()
            count += 1

            # 그 요소가 출력 순서를 알고자하는 대상인 경우
            if position == 0:
                print(count)
                break
            # 우선순위 최대값 갱신
            elif docs:
                top_priority = max(docs)
        # 큐 맨앞의 요소가 최고 우선순위를 가지지 않는 경우
        else:
            docs.append(docs.popleft())

            # # 그 요소가 출력 순서를 알고자하는 대상인 경우, 위치 정보 갱신
            if position == 0:
                position = len(docs)

        position -= 1
