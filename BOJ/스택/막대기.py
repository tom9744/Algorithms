from sys import stdin

N = int(stdin.readline().rstrip())
stack = [int(stdin.readline().rstrip()) for _ in range(N)]
curr_in_sight = 0
result = 0

while stack:
    top = stack.pop()

    # 현재 눈에 보이는 최대 높이의 막대보다 높은 막대면, 결과에 추가한다.
    if top > curr_in_sight:
        curr_in_sight = top  # 시야 내 최대 높이 갱신
        result += 1

print(result)
