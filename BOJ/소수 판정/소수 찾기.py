N = int(input())  # 숫자는 1,000 이하의 자연수

# 범위 내의 모든 숫자에 대한 소수 여부를 나타내는 배열(= 리스트)
is_prime = [True for _ in range(1001)]
is_prime[0], is_prime[1] = False, False

# 1,000까지 모든 수를 검사할 필요 없이, 1000^(1/2)까지만 검사하면 된다.
for number in range(2, int(1001 ** 0.5) + 1):
    # 소수인 숫자의 모든 배수는 소수가 아니다.
    if is_prime[number]:
        # 현재 숫자의 모든 배수에 대해, 소수가 아님을 표시한다.
        for multiple in range(number + number, 1001, number):
            is_prime[multiple] = False

# 소수 판별을 하고 싶은 숫자를 입력 받는다.
targets = list(map(int, input().split()))
count = 0

# is_prime[숫자]로 조회하면, 소수 여부를 알 수 있다.
for target in targets:
    if is_prime[target]:
        count +=1

print(count)
