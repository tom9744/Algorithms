from itertools import permutations

N = int(input())
numbers = list(map(int, input().split()))
operators = []

for index, each in enumerate(list(map(int, input().split()))):
    if index == 0:
        pluses = ["+" for _ in range(each)]
        operators.extend(pluses)
    elif index == 1:
        minuses = ["-" for _ in range(each)]
        operators.extend(minuses)
    elif index == 2:
        multiplies = ["*" for _ in range(each)]
        operators.extend(multiplies)
    elif index == 3:
        divides = ["/" for _ in range(each)]
        operators.extend(divides)

permute = list(permutations(operators, N - 1))
max_result = -1000000001
min_result = 1000000001

for case in permute:
    result = numbers[0]

    for index in range(N - 1):
        next_number = numbers[index + 1]
        oper = case[index]

        if oper == "+":
            result += next_number

        elif oper == "-":
            result -= next_number

        elif oper == "*":
            result *= next_number

        elif oper == "/":
            result //= next_number

    if result > max_result:
        max_result = result
    if result < min_result:
        min_result = result

print(max_result)
print(min_result)