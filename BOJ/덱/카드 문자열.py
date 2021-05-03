from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    cards = input().split(" ")  # 알파벳이 적힌 카드들
    string = deque(cards[0])    # 알파벳 카드를 이용해 만들 문자열

    for alpha in cards[1:]:
        # 사전 순으로 빠른 문자인 경우, 데크의 앞에 삽입한다.
        if ord(alpha) <= ord(string[0]):
            string.appendleft(alpha)
        # 그렇지 않은 경우, 데크의 뒤에 삽입한다.
        else:
            string.append(alpha)

    print("".join(string))