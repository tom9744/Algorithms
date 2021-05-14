import collections

T = int(input())

for _ in range(T):
    case = list(input())

    left = collections.deque()
    right = collections.deque()

    for char in case:
        # 왼쪽 배열(= 스택)에서 오른쪽 배열(= 덱)로 요소를 옮긴다.
        if char == "<":
            if left:
                right.appendleft(left.pop())
        # 오른쪽 배열에서 왼쪽 배열로 요소를 옮긴다.
        elif char == ">":
            if right:
                left.append(right.popleft())
        # 왼쪽 배열에서 맨 마지막 요소를 제거한다.
        elif char == "-":
            if left:
                left.pop()
        # 명령어가 아닌 경우, 왼쪽 배열에 삽입한다.
        else:
            left.append(char)

    # 두 배열을 합쳐서 출력한다.
    print("".join(left + right))



