# 6588: 골드바흐의 추측
#
# 1,000,000까지의 모든 소수를 에라토스테네스의 체를 이용해 구한뒤 입력된 짝수를 소수로 만들 수 있는지 판단하면 된다.
#
# 이 때, combinations 또는 반복문을 사용해 모두 비교하면 시간초과가 발생하였다.
# 따라서 소수 N이 있을 때, 다른 소수는 (짝수 - N)이라는 점에서 착안해 문제를 풀어야 한다.
#
# 6 = 3 + 3과 같이, 동일한 소수를 두 번 사용해도 되기 때문에 반복문의 'range'를
# (even_number // 2)가 아닌 ((even_number // 2) + 1)으로 설정해 주어야 한다.

numbers = [i for i in range(1000001)]
numbers[1] = 0

for index in range(2, 1000001):
    if numbers[index] == 0:
        continue

    for number in range(index * 2, 1000001, index):
        numbers[number] = 0

while True:
    even_number = int(input())

    if even_number == 0:
        break

    is_possible = False
    min_prime = 0

    for num in range((even_number // 2) + 1):
        if numbers[num] != 0 and numbers[even_number - num] != 0:
            min_prime = numbers[num]
            is_possible = True
            break

    if is_possible:
        print(str(even_number) + " = " + str(min_prime) + " + " + str(even_number - min_prime))
    else:
        print("Goldbach's conjecture is wrong.")