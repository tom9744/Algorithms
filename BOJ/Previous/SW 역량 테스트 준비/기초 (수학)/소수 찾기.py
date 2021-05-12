# 1978: 소수 찾기
#
# 소수를 구해야하는 수의 범위가 정해져 있으므로, 아리스토테네스의 체를 이용해 빠르게 구한다.
#
# 이후 입력으로 들어온 수의 인덱스를 비교하여, 0이 아닌 경우(= 소수인 경우) 계수에 반영한다.

numbers = [num for num in range(1001)]  # N은 1000 이하
numbers[1] = 0

# 아리스토테네스의 체를 이용한 소수 구하기
for current_number in range(2, 1001):
    if numbers[current_number] == 0:
        continue

    for number in range(current_number + current_number, 1001, current_number):
        numbers[number] = 0


N = int(input())
input_numbers = list(map(int, input().split()))
count = 0

for each in input_numbers:
    if numbers[each] != 0:
        count += 1

print(count)
