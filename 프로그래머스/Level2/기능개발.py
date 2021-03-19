# 코딩테스트 연습 > 스택/큐 > 기능개발 (Level2)
def solution(progresses, speeds):
    answer = []

    while progresses:
        # 진척도를 반영한다.
        for idx, val in enumerate(progresses):
            progresses[idx] = 100 if val + speeds[idx] > 100 else val + speeds[idx]

        # 가장 앞 작업의 진척도가 100이 된 경우,
        if progresses[0] == 100:
            count = 0
            # 연속적으로 진척도가 100인 작업의 개수를 센다
            for idx, val in enumerate(progresses):
                if val == 100:
                    count += 1
                else:
                    break
            answer.append(count)  # 정답에 추가한다.
            progresses = progresses[count:]  # 작업 완료된 부분을 제거한다.
            speeds = speeds[count:]  # 작업 완료된 부분을 제거한다.

    return answer


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # 1, 3, 2
