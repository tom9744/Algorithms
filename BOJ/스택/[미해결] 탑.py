N = int(input())
towers = input().split(" ")
stack = []
result = [0] * len(towers)

# 탑의 높이가 저장된 배열을 뒤집어, 마지막 탑부터 시작한다.
for idx, current_tower_height in enumerate(reversed(towers)):
    # 스택에 현재 탑보다 높이가 낮은 탑이 있는 경우,
    while stack and current_tower_height > towers[stack[-1]]:
        last = stack.pop()  # 스택에서 해당 탑의 위치(= 인덱스)를 꺼낸다.
        result[last] = len(towers) - idx  # 현재 탑의 위치를 결과에 저장한다.
    stack.append(len(towers) - idx - 1)  # 스택에 현재 탑의 위치를 삽입한다.

    print(stack, result)

print(" ".join(map(str, result)))

# 반례
# 5
# 10 3 4 5 8
# [4] [0, 0, 0, 0, 0]
# [4, 3] [0, 0, 0, 0, 0]
# [4, 3, 2] [0, 0, 0, 0, 0]
# [4, 3, 2, 1] [0, 0, 0, 0, 0]
# [4, 3, 2, 1, 0] [0, 0, 0, 0, 0]
# result : 0 0 0 0 0
# answer : 0 1 2 3 4