T = int(input())

for _ in range(T):
    number = int(input())
    ones = []

    bit_position = 0
    while number > 0:
        remainder = number % 2  # 현재 수를 2로 나눈 나머지
        number //= 2            # 현재 수를 2로 나눈 몫으로 갱신

        # 나머지가 0이 아닌 경우, 현재 비트는 1이 되어야 한다.
        if remainder:
            ones.append(str(bit_position))  # 현재 비트 번호 기록

        bit_position += 1

    print(" ".join(ones))
