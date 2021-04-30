N = int(input())
result = 0

for _ in range(N):
    word = input()
    stack = []

    # 홀수는 쌍을 이룰 수 없으므로 스킵한다.
    if len(word) % 2 != 0:
        continue

    for idx, char in enumerate(word):
        # 현재 문자와 스택 맨 위의 문자가 같으면 꺼낸다.
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    # 스택이 완전히 비워지면, 쌍이 맞는 것이다.
    if not stack:
        result += 1

print(result)