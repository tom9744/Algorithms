# '커서'를 스택으로 추상화한 풀이 (통과)
from sys import stdin

stack = list(stdin.readline().rstrip())
memory_stack = []  # pop()을 이용해 커서가 이동할 때 제거된 원소들의 임시 저장 공간
M = int(stdin.readline().rstrip())

for _ in range(M):
    command = stdin.readline().rstrip().split(" ")

    # 원본 스택에서 원소를 꺼내 메모리 스택으로 이동
    if command[0] == "L":
        if stack:
            memory_stack.append(stack.pop())
    # 메모리 스택에서 원소를 꺼내 원본 스택으로 이동
    if command[0] == "D":
        if memory_stack:
            stack.append(memory_stack.pop())
    # 원본 스택에서 원소 제거
    if command[0] == "B":
        if stack:
            stack.pop()
    # 원본 스택에 원소 추가
    if command[0] == "P":
        stack.append(command[1])

# 임시 저장된 원소를 스택에서 모두 꺼내 원본 스택에 추가
while memory_stack:
    stack.append(memory_stack.pop())

print("".join(stack))


# 문제에서 주어진 대로만 구현한 풀이 (시간 초과)
string = stdin.readline().rstrip()
M = int(stdin.readline().rstrip())
cursor = len(string)

for _ in range(M):
    command = stdin.readline().rstrip().split(" ")

    if command[0] == "L":
        if cursor > 0:
            cursor -= 1
    if command[0] == "D":
        if cursor < len(string):
            cursor += 1
    if command[0] == "B":
        if cursor == 0:
            continue
        else:
            string = string[:cursor - 1] + string[cursor:]
        cursor -= 1
    if command[0] == "P":
        if cursor == len(string):
            string = string + command[1]
        else:
            string = string[:cursor] + command[1] + string[cursor:]
        cursor += 1

print(string)
