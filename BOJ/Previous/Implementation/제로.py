# 10773 : 제로
#
# 입력된 수를 스택에 보관하다가 0이 입력되면 맨 위에서 하나를 꺼낸다.
# 마지막에 스택에 남은 원소 합을 구하면 된다.

K = int(input())
stack = []

for _ in range(K):
    number = int(input())

    if number == 0:
        stack.pop()
    else:
        stack.append(number)

result = sum(stack)
print(result)