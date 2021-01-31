N = int(input())

temp = N
count = 0

while True:

    if count != 0 and temp == N:
        break

    if temp < 10:
        temp = temp * 11
    else:
        string = str(temp)
        ten, one = string[0], string[1]

        summary = str(int(ten) + int(one))

        merge = one + summary[-1]

        temp = int(merge)

    count += 1

print(count)