def main():
    N = int(input())

    stack, result = [], []
    is_valid = True
    curr = 1

    def add():
        result.append("+")
        stack.append(curr)

    def remove():
        stack.pop()
        result.append("-")

    for _ in range(N):
        num = int(input())

        # 스택이 비어있는 경우, 일단 값을 하나 채운다.
        if not stack:
            add()
            curr += 1

        # 스택의 마지막 값이 현재 수보다 작은 경우, 그 수가 될 때까지 push()한다.
        if stack and stack[-1] < num:
            while stack[-1] < num:
                add()
                curr += 1

        # 스택의 마지막 값이 현재 수와 같은 경우, pop()한다.
        if stack and stack[-1] == num:
            remove()

        # 스택의 마지막 값보다 현재 수가 크면, 만들 수 없는 수열이므로 종료한다.
        if stack and stack[-1] > num:
            is_valid = False
            break

    if is_valid:
        for each in result:
            print(each)
    else:
        print("NO")


if __name__ == '__main__':
    main()
