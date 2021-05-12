# 9009 : 피보나치
#
# 가장 먼저 주어진 숫자까지의 피보나치 수열을 구해본다.
# 이후, 주어진 숫자에서 피보나치 수열 중 가장 큰 숫자부터 이용해 뺄셈을 수행해 본다.
# (주어진 숫자 - i번째 큰 피보나치 수) > 0인 경우에만 결과 배열에 해당 피보나치 수를 추가한다.
# (주어진 숫자 - i번째 큰 피보나치 수) = 0인 경우, 해당 피보나치 수를 배열에 추가하고 반복문을 종료한다.

num_of_data = int(input())
data = []

for _ in range(num_of_data):
    data.append(int(input()))

for number in data:
    fibonacci_array = [0, 1]
    current = 0
    position = 0
    while current <= number:
        current = fibonacci_array[position] + fibonacci_array[position + 1]
        position += 1
        fibonacci_array.append(current)

    result = []

    for index in range(1, len(fibonacci_array)):
        fibonacci = fibonacci_array[len(fibonacci_array) - index - 1]

        if number - fibonacci == 0:
            result.append(fibonacci)
            break
        elif number - fibonacci > 0:
            number -= fibonacci
            result.append(fibonacci)

    result.sort()

    print(" ".join(map(str, result)))