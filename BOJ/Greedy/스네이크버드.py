# 16435 : 스네이크버드
#
# 과일의 높이를 오름차순으로 정렬한 뒤, 현재 뱀의 길이와 비교하면서
# 뱀의 길이보다 작은 경우 뱀의 길이에 1을 더한다.
# 만약 뱀의 길이보다 높은 과일을 만나면 반복문을 종료하고 결과를 출력한다.

num_of_fruits, length_of_snake = map(int, input().split())
heights = list(map(int, input().split()))

heights.sort()

for height in heights:
    if height <= length_of_snake:
        length_of_snake += 1
    else:
        break

print(length_of_snake)