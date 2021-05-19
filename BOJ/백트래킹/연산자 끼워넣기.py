N = int(input())
numbers = list(map(int, input().split()))
operands = list(map(int, input().split()))


def DFS(value, index):
    global max_value, min_value

    # 숫자를 모두 다 사용한 경우, 최대/최소 값을 갱신하고 종료한다.
    if index == len(numbers):
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return

    # 사용 가능한 연산자가 존재하는 경우, 해당 연산자를 사용해 계산하고 DFS 함수를 재귀호출 한다.
    if operands[0] > 0:
        operands[0] -= 1  # 사용 가능한 연산자 수 감소
        DFS(value + numbers[index], index + 1)
        operands[0] += 1  # 백트래킹

    if operands[1] > 0:
        operands[1] -= 1
        DFS(value - numbers[index], index + 1)
        operands[1] += 1

    if operands[2] > 0:
        operands[2] -= 1
        DFS(value * numbers[index], index + 1)
        operands[2] += 1

    if operands[3] > 0:
        operands[3] -= 1
        # 음수를 양수로 나누는 경우, C++14의 기준을 따른다.
        if value < 0:
            quotient = -value // numbers[index]
            DFS(-quotient, index + 1)
        else:
            DFS(value // numbers[index], index + 1)
        operands[3] += 1


max_value = -float("inf")
min_value = float("inf")

DFS(numbers[0], 1)

print(max_value)
print(min_value)
