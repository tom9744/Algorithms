# 13413 : 오셀로 재배치
#
# 현재 상태와 목표 상태의 배치를 비교하여, W와 B에 대해 각각 몇개가 다른지 파악한다.
# 예를 들어 W로 바뀌어야할 것이 3개, B로 바뀌어야할 것이 4개인 경우,
# 두 오셀로의 위치를 교환하는 연산 3회 + 한 오셀로의 색상을 변경하는 연산 1회로 총 4회 안에 목표 상태에 도달할 수 있다.

test_case = int(input())

for case in range(test_case):

    num_of_othello = int(input())
    init = input()
    goal = input()

    b_to_w, w_to_b = 0, 0

    for index in range(num_of_othello):
        if goal[index] != init[index] and goal[index] == "W":
            b_to_w += 1
        elif goal[index] != init[index] and goal[index] == "B":
            w_to_b += 1

    case_1 = min(b_to_w, w_to_b)
    case_2 = abs(b_to_w - w_to_b)

    print(case_1 + case_2)