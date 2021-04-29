import sys

N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N):
    command_line = sys.stdin.readline().rstrip().split(" ")

    if command_line[0] == "push":
        stack.append(command_line[1])
    elif command_line[0] == "pop":
        if len(stack) == 0:
            print(-1)
            continue
        print(stack.pop())
    elif command_line[0] == "size":
        print(len(stack))
    elif command_line[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    elif command_line[0] == "top":
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[-1])
