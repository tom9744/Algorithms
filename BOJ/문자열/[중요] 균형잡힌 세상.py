import sys, re

while True:
    line = sys.stdin.readline().rstrip()

    if line == ".":
        break

    brackets = re.sub(r'[^()\[\]]', "", line)  # 괄호를 제외한 모든 문자 삭제
    pairs = {"(": ")", "[": "]"}
    stack = []
    is_balanced = True

    # 여는 괄호인 경우 스택에 넣고, 닫는 괄호인 경우 스택의 맨 위를 확인
    for bracket in brackets:
        if bracket == "(" or bracket == "[":
            stack.append(bracket)
        else:
            # 스택이 비었거나, 맨 위의 괄호가 닫는 괄호와 매칭되지 않으면 반복문을 종료한다.
            if not stack or bracket != pairs[stack[-1]]:
                is_balanced = False
                break
            stack.pop()

    # 반복문이 종료되는 시점에 스택에 괄호가 남아있으면 짝이 맞지 않는 것이다.
    if stack:
        is_balanced = False

    print("yes" if is_balanced else "no")