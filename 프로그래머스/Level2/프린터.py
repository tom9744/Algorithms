# 코딩테스트 연습 > 스택/큐 > 프린터 (Level2)


def solution(priorities, location):
    answer = 0

    while True:
        max_priority = max(priorities)  # 현재의 최대 우선순위 값

        current = priorities.pop(0)  # 대기목록에서 맨앞에 있는 것을 꺼낸다.

        # 방금 꺼낸 것이 최대의 우선순위를 가지는 경우,
        if current == max_priority:
            answer += 1  # 프린트 횟수 1 증가
            if location == 0:
                break  # 내 문서인 경우 반복문 종료
            else:
                location -= 1  # 내 문서가 아닌 경우 내 문서 위치 1만큼 감소
        # 방금 꺼낸 것이 최대 우선순위가 아닌 경우,
        else:
            priorities.append(current)  # 대기목록에 다시 넣는다.
            if location == 0:
                location = len(priorities) - 1  # 내 문서인 경우, 위치 갱신
            else:
                location -= 1  # 내 문서가 아닌 경우, 내 문서 위치 1만큼 감소

    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
