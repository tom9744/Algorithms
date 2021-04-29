def main():
    pairs = {")": "(", "]": "["}
    values = {")": 2, "]": 3}

    brackets = input()
    stack = []

    for bracket in brackets:
        # 여는 괄호는 즉시 스택에 삽입한다.
        if bracket == "(" or bracket == "[":
            stack.append(bracket)
            continue
        else:
            # 닫는 괄호가 여는 괄호보다 많은 경우, 바로 0을 반환한다.
            if not stack:
                return 0

            acc = 0
            while stack:
                current = stack.pop()  # 스택의 맨 위 원소를 꺼낸다.

                # 현재 닫는 괄호의 짝을 발견한 경우, 사이값에 알맞는 값을 곱해 스택에 삽입한다.
                if current == pairs[bracket]:
                    stack.append(values[bracket] * (acc if acc > 0 else 1))
                    break
                # 여는 괄호지만 짝이 맞지 않은 경우, 바로 0을 반환한다.
                elif current == "(" or current == "[":
                    return 0
                # 숫자 값을 만나는 경우, 누적한다. (()()) = (2 + 2) = (4) = 2 * 4
                else:
                    acc += current

    # 여는 괄호가 스택에 남아 있는 경우, 0을 반환한다.
    if "(" in stack or "[" in stack:
        return 0

    return sum(stack)


if __name__ == '__main__':
    result = main()
    print(result)