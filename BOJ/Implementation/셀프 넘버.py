# 4673 : 셀프 넘버


def generate(n):
    digits = list(str(n))
    temp = 0

    for digit in digits:
        temp += int(digit)

    return n + temp


has_constructor = [False for _ in range(10000)]
number = 1

while number <= 10000:
    new_number = generate(number)

    if new_number <= 10000:
        has_constructor[new_number - 1] = True

    number += 1

for idx in range(10000):
    if not has_constructor[idx]:
        print(idx + 1)
