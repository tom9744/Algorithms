import collections

N = int(input())
cards = collections.deque([num for num in range(1, N + 1)])

while len(cards) > 1:
    cards.popleft()  # 1. 카드를 버린다.
    cards.append(cards.popleft())  # 2. 카드를 제일 아래로 옮긴다.

print(cards.pop())