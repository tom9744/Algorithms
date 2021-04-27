def using_stack():
    T = int(input())

    for _ in range(T):
        # 길이가 2 이상이므로, 빈 문자열에 대한 예외처리는 하지 않는다.
        parenthesis = input()
        stack = []
        is_valid = True

        for each in parenthesis:
            if each == "(":
                stack.append(each)
            else:
                # 스택이 비어있어, 꺼낼 원소가 없다면 유효하지 않은 것이다.
                if not stack:
                    is_valid = False
                    break
                stack.pop()

        # 반복문이 종료되었을 때, 스택에 원소가 남아있다면 유효하지 않은 것이다.
        if stack:
            is_valid = False

        print("YES" if is_valid else "NO")


def without_stack():
    T = int(input())

    for _ in range(T):
        # 길이가 2 이상이므로, 빈 문자열에 대한 예외처리는 하지 않는다.
        parenthesis = input()
        is_valid = True
        count = 0

        for each in parenthesis:
            if each == "(":
                count += 1
            else:
                count -= 1
                # count 값이 음수이면, "("보다 ")"가 많은 것이므로 유효하지 않다.
                if count < 0:
                    is_valid = False
                    break

        # 반복문 종료 시점에 count 값이 양수이면, "("가 ")"보다 많은 것이므로 유효하지 않다.
        if count > 0:
            is_valid = False

        print("YES" if is_valid else "NO")
