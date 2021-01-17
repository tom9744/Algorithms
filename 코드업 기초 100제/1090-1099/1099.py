# 1099 : [기초-2차원배열] 성실한 개미

cage = []

for _ in range(10):
    row = list(map(int, input().split()))
    cage.append(row)

current_x = 1
current_y = 1

while True:
    origin = cage[current_x][current_y]
    cage[current_x][current_y] = 9

    if origin is 2:
        break

    if current_x is 9 and current_y is 9:
        break

    if cage[current_x + 1][current_y] is 1 and cage[current_x][current_y + 1] is 1:
        break

    cage[current_x][current_y] = 9

    if cage[current_x][current_y + 1] is not 1:
        current_y += 1
    elif cage[current_x + 1][current_y] is not 1:
        current_x += 1


for row in cage:
    for item in row:
        print(item, end=" ")
    print()




