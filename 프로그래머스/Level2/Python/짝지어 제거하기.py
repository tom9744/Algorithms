def solution(s):
    stack = [s[0]]

    for char in s[1:]:
        # 스택의 마지막 요소와 현재 문자가 같은 경우, 스택에서 제거한다.
        if stack and char == stack[-1]:
            stack.pop()
        # 그렇지 않은 경우, 스택에 추가한다.
        else:
            stack.append(char)

    # 스택을 모두 비울 수 있으면 짝지어 제거하기 가능!
    return 1 if len(stack) == 0 else 0
