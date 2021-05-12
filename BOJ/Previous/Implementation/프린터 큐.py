# 1966 : 프린터 큐
#
# 목표 문서의 위치를 저장하는 변수 `current_position`와 우선순위를 저장하는 변수 `priority`를 통해 값을 기억해 놓는다.
# 반복문을 돌면서 Queue 맨 앞의 문서를 꺼내보고, 최대 우선순위와 같은 우선순위를 가지는 문서인 경우 Queue 에서 제거한다.
# 최대 우선순위보다 작은 우선순위인 경우, Queue 맨 뒤로 이동시키고 `current_position`의 값을 1만큼 감소시킨다.
#
# `current_position`가 0이라면 목표 문서의 우선순위가 최대값과 동일한지 비교하고, 같다면 바로 인쇄하고 반복문을 끝낸다.
# 같지 않다면, 현재 문서를 Queue 맨 뒤로 이동하고 `current_position` 값을 (Queue 길이 - 1)로 갱신한다.

T = int(input())

for _ in range(T):

    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    current_position = M
    priority = queue[M]
    count = 0

    while len(queue) != 0:
        highest = max(queue)
        front = queue.pop(0)

        # 목표 문서가 현재 Queue 맨 앞에 있는 경우
        if current_position == 0:
            # 최대 우선순위라면 종료
            if priority == highest:
                count += 1
                break
            # Queue 맨 뒤로 이동 후, `current_position` 갱신
            else:
                queue.append(front)
                current_position = len(queue) - 1
        # Queue 맨 앞의 문서가 목표 문서가 아닌 경우
        else:
            # 목표 문서의 위치를 1만큼 앞으로 이동
            current_position -= 1

            # 최대 우선순위라면 인쇄 실시
            if front == highest:
                count += 1
            # Queue 맨 뒤로 이동
            else:
                queue.append(front)

    print(count)