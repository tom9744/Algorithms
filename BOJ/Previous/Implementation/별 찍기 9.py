# 2446 : 별 찍기 - 9

N = int(input())

stack = []

for idx in range(N):

    stars = "*" * ((2 * N) - 1 - (2 * idx))
    spaces = " " * idx

    line = spaces + stars

    if idx != N - 1:
        stack.append(line)

    print(line)

while len(stack) != 0:
    print(stack.pop())