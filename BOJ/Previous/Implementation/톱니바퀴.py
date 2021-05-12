# 14891 : 톱니바퀴

def rotate(target, direction):

    # 시계 방향
    if direction == 1:
        tail = target.pop()
        target.insert(0, tail)
    # 반시계 방향
    elif direction == -1:
        head = target.pop(0)
        target.append(head)


# 오른쪽 톱니바퀴가 회전 가능한지 검사한다.
def check_right(number, direction):
    if number > 4 or gears[number - 2][2] == gears[number - 1][6]:
        return

    if gears[number - 2][2] != gears[number - 1][6]:
        check_right(number + 1, -direction)
        rotate(gears[number - 1], direction)


# 왼쪽 톱니바퀴가 회전 가능한지 검사한다.
def check_left(number, direction):
    if number < 1 or gears[number - 1][2] == gears[number][6]:
        return

    if gears[number - 1][2] != gears[number][6]:
        check_left(number - 1, -direction)
        rotate(gears[number - 1], direction)


# 12시부터 0번째...오른쪽 인덱스 2 / 왼쪽 인덱스 6
gears = []

for _ in range(4):
    gears.append(list(map(int, input())))

K = int(input())

for _ in range(K):
    number, direction = map(int, input().split())

    # 회전을 수행하기 이전에 양쪽에 대해 회전 여부 검사를 수행한다.
    check_right(number + 1, -direction)
    check_left(number - 1, -direction)
    rotate(gears[number - 1], direction)

result = 0

for idx in range(4):
    result += 2 ** idx if gears[idx][0] == 1 else 0

print(result)