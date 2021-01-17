# 2839 : 설탕배달

total_weight = int(input())
number_of_bags = 0

while True:
    if total_weight % 5 is 0:
        number_of_bags += total_weight // 5
        print(number_of_bags)
        break

    total_weight -= 3
    number_of_bags += 1

    if total_weight < 0:
        print(-1)
        break