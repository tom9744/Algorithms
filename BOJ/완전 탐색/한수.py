def is_isometric(numbers):
    length = len(numbers)

    if length < 3:
        return True

    gap = int(numbers[1]) - int(numbers[0])
    for idx in range(2, length):
        if int(numbers[idx]) - int(numbers[idx - 1]) != gap:
            return False

    return True


N = int(input())
count = 0

# 1부터 N까지 완전탐색한다.
for num in range(1, N + 1):
    if is_isometric(str(num)):
        count += 1

print(count)
