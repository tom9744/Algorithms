from collections import deque

N = int(input())
skills = list(map(int, input().split(" ")))

# 현재 카드 상태(current)와 처음 카드 상태(origin)
current = deque([i for i in range(1, N + 1)])
origin = deque()

for _ in range(N):
    top = current.popleft()  # 현재 카드 상태 중 맨 위에 있는 카드
    skill = skills.pop()     # 가장 마지막에 사용한 기술

    if skill == 1:
        # 처음 카드 상태의 맨 위에 카드를 넣는다.
        origin.appendleft(top)
    if skill == 2:
        # 처음 카드 상태의 맨 위에서 두번째 위치에 카드를 넣는다.
        temp = origin.popleft()
        origin.appendleft(top)
        origin.appendleft(temp)
    if skill == 3:
        # 처음 카드 상태의 맨 뒤에 카드를 넣는다.
        origin.append(top)

for card in origin:
    print(card, end=" ")
