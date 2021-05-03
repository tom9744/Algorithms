from collections import deque

N = int(input())
balloons = deque([(i + 1, n) for i, n in enumerate(map(int, input().split(" ")))])

number, value = balloons.popleft()  # 제일 처음에는 1번 풍선을 터트린다.
result = [number, ]

# 터트린 풍선에서 나온 숫자 value 만큼 데크를 회전(?)시킨다.
while balloons:
    if value > 0:
        for _ in range(value - 1):
            temp = balloons.popleft()
            balloons.append(temp)
        num, val = balloons.popleft()
    else:
        for _ in range(abs(value) - 1):
            temp = balloons.pop()
            balloons.appendleft(temp)
        num, val = balloons.pop()

    result.append(num)  # 터트린 풍선 번호를 배열에 추가한다.
    value = val         # 터트린 풍선에서 나온 숫자를 갱신한다.

for each in result:
    print(each, end=" ")