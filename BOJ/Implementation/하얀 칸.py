count = 0

for row in range(8):
    alignment = list(input())

    for col in range(8):
        if row % 2 == 0:
            if col % 2 == 0 and alignment[col] == "F":
                count += 1
        else:
            if col % 2 == 1 and alignment[col] == "F":
                count += 1

print(count)