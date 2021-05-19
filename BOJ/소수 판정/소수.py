M = int(input())
N = int(input())

is_prime = [True for _ in range(10001)]
is_prime[0], is_prime[1] = False, False

# 에라토스테네스의 체 알고리즘으로 모든 범위의 수에 대해 소수 판별을 수행한다.
for number in range(2, int(10001 ** 0.5) + 1):
    if is_prime[number]:
        for multiple in range(number + number, 10001, number):
            is_prime[multiple] = False

min_prime, prime_sum, does_exist = float("inf"), 0, False

# 범위 안의 숫자에 대해 소수 여부를 확인한다.
for num in range(M, N + 1):
    if is_prime[num]:
        min_prime = min(min_prime, num)
        prime_sum += num
        does_exist = True

# 소수가 존재하는 경우와 그렇지 않은 경우에 대해 적절한 답안을 출력한다.
if does_exist:
    print(prime_sum)
    print(min_prime)
else:
    print(-1)
