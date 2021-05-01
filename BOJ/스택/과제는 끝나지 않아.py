from sys import stdin

N = int(stdin.readline().rstrip())
stack = []
result = 0

for _ in range(N):
    assignment = list(map(int, stdin.readline().rstrip().split(" ")))

    # 과제가 주어진 경우, 스택의 맨 위에 추가한다.
    if assignment[0] == 1:
        stack.append([assignment[1], assignment[2]])  # [점수, 소요시간]

    # 스택에 원소가 존재하는 경우,
    if stack:
        stack[-1][1] -= 1  # 시간 경과 처리

        # 소요 시간이 모두 경과한 경우, 스택에서 제거하고 점수를 결과에 추가한다.
        if stack[-1][1] == 0:
            result += stack.pop()[0]

print(result)
