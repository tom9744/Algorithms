string = input()
bomb = input()

L = len(bomb)  # 폭탄 문자열 길이
stack = []

for char in string:
    stack.append(char)

    # 폭탄 문자열이 발견된 경우,
    if len(stack) >= L and "".join(stack[-L:]) == bomb:
        # 폭탄 문자열 길이만큼 스택에서 요소를 꺼낸다.
        for _ in range(L):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
