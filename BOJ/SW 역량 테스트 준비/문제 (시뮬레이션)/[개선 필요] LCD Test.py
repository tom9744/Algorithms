# 2290: LCD Test
#
# 정답을 맞추긴 했지만, 중복되는 부분에 대한 처리를 추가하는 개선이 필요하다.

s, n = map(int, input().split())
height = (2 * s) + 3
width = s + 2
display = [[] for _ in range(height)]

for number in str(n):

    if number == "1":
        for h in range(height):
            temp = [" "] * width
            if h == 0 or h == height - 1 or h == height // 2:
                display[h].append("".join(temp))
            else:
                temp[width - 1] = "|"
                display[h].append("".join(temp))
    if number == "2":
        for h in range(height):
            if h == 0 or h == height - 1 or h == height // 2:
                temp = ["-"] * width
                temp[0], temp[width - 1] = " ", " "
                display[h].append("".join(temp))
            elif h < height // 2:
                temp = [" "] * width
                temp[width - 1] = "|"
                display[h].append("".join(temp))
            else:
                temp = [" "] * width
                temp[0] = "|"
                display[h].append("".join(temp))
    if number == "3":
        for h in range(height):
            if h == 0 or h == height - 1 or h == height // 2:
                temp = ["-"] * width
                temp[0], temp[width - 1] = " ", " "
                display[h].append("".join(temp))
            else:
                temp = [" "] * width
                temp[width - 1] = "|"
                display[h].append("".join(temp))
    if number == "4":
        for h in range(height):
            if h == 0 or h == height - 1:
                temp = [" "] * width
                display[h].append("".join(temp))
            elif h == height // 2:
                temp = ["-"] * width
                temp[0], temp[width - 1] = " ", " "
                display[h].append("".join(temp))
            elif h < height // 2:
                temp = [" "] * width
                temp[0], temp[width - 1] = "|", "|"
                display[h].append("".join(temp))
            else:
                temp = [" "] * width
                temp[width - 1] = "|"
                display[h].append("".join(temp))
    if number == "5":
        for h in range(height):
            if h == 0 or h == height - 1 or h == height // 2:
                temp = ["-"] * width
                temp[0], temp[width - 1] = " ", " "
                display[h].append("".join(temp))
            elif h > height // 2:
                temp = [" "] * width
                temp[width - 1] = "|"
                display[h].append("".join(temp))
            else:
                temp = [" "] * width
                temp[0] = "|"
                display[h].append("".join(temp))
    if number == "6":
        for h in range(height):
            if h == 0 or h == height - 1 or h == height // 2:
                temp = ["-"] * width
                temp[0], temp[width - 1] = " ", " "
                display[h].append("".join(temp))
            elif h > height // 2:
                temp = [" "] * width
                temp[0], temp[width - 1] = "|", "|"
                display[h].append("".join(temp))
            else:
                temp = [" "] * width
                temp[0] = "|"
                display[h].append("".join(temp))
    if number == "7":
        for h in range(height):
            if h == 0:
                temp = ["-"] * width
                temp[0], temp[width - 1] = " ", " "
                display[h].append("".join(temp))
            elif h == height - 1 or h == height // 2:
                temp = [" "] * width
                display[h].append("".join(temp))
            else:
                temp = [" "] * width
                temp[width - 1] = "|"
                display[h].append("".join(temp))
    if number == "8":
        for h in range(height):
            if h == 0 or h == height - 1 or h == height // 2:
                temp = ["-"] * width
                temp[0], temp[width - 1] = " ", " "
                display[h].append("".join(temp))
            else:
                temp = [" "] * width
                temp[0], temp[width - 1] = "|", "|"
                display[h].append("".join(temp))
    if number == "9":
        for h in range(height):
            if h == 0 or h == height - 1 or h == height // 2:
                temp = ["-"] * width
                temp[0], temp[width - 1] = " ", " "
                display[h].append("".join(temp))
            elif h < height // 2:
                temp = [" "] * width
                temp[0], temp[width - 1] = "|", "|"
                display[h].append("".join(temp))
            else:
                temp = [" "] * width
                temp[width - 1] = "|"
                display[h].append("".join(temp))
    if number == "0":
        for h in range(height):
            if h == 0 or h == height - 1:
                temp = ["-"] * width
                temp[0], temp[width - 1] = " ", " "
                display[h].append("".join(temp))
            elif h == height // 2:
                temp = [" "] * width
                display[h].append("".join(temp))
            else:
                temp = [" "] * width
                temp[0], temp[width - 1] = "|", "|"
                display[h].append("".join(temp))

for idx in range(height):
    print(" ".join(display[idx]))
