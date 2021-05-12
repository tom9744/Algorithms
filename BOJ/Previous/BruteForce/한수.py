N = int(input())
count = 0

for number in range(1, N + 1):
    if number < 100:
        count += 1
    elif 100 <= number < 1000:
        digits = list(map(int, list(str(number))))

        if (digits[2] - digits[1]) == (digits[1] - digits[0]):
            count += 1
    else:
        pass

print(count)