# 2960 : 에라토스테네스의 체

N, K = map(int, input().split())

# 1. 2부터 N까지 모든 정수를 적는다.
numbers = [num for num in range(2, N + 1)]
primes = []
count = 0

while len(numbers) != 0:
    # 2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
    prime = numbers[0]
    primes.append(prime)

    # 3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
    for number in numbers:
        if number % prime == 0:
            count += 1
            numbers.remove(number)
            if count == K:
                print(number)

    # 4. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.


