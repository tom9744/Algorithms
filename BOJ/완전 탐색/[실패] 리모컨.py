N = int(input())
M = int(input())

is_broken = {
    0: False, 1: False, 2: False, 3: False, 4: False,
    5: False, 6: False, 7: False, 8: False, 9: False,
}

if M > 0:
    for broken_number in input().split():
        is_broken[int(broken_number)] = True

current = 100
min_count = abs(N - current)  # "+", "-"만 사용해서 채널을 바꾸는 방법

temp = []
count = 0

# 목표 채널에 가장 근사한 채널 번호로 이동한다.
for num in str(N):
    num = int(num)

    if is_broken[num]:
        left_number, right_number = -1, -1

        # 현재 수보다 작은 수를 탐색한다.
        for left in range(num - 1, -1, -1):
            if not is_broken[left]:
                left_number = left
                break
        # 현재 수보다 큰 수를 탐색한다.
        for right in range(num + 1, 10):
            if not is_broken[right]:
                right_number = right
                break

        # 현재 수에서 작은 수, 큰 수로의 거리를 각각 구한다.
        left_gap, right_gap = abs(num - left_number), abs(num - right_number)

        # 현재 수에 보다 가까운(= 값 차이가 작은) 숫자를 선택한다.
        temp.append(str(left_number) if left_gap < right_gap else str(right_number))
    else:
        temp.append(str(num))

    count += 1  # 리모컨을 누른 횟수를 1 증가 시킨다.


# 현재 채널과 가장 가까운 채널
selected = int("".join(temp))

if selected == 0:
    count = 1

count += abs(N - selected)

min_count = min(min_count, count)

print(min_count)
