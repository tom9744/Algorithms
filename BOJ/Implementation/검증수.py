# 2475 : 검증수

numbers = list(map(int, input().split()))
verification_number = 0

for num in numbers:
    verification_number += num ** 2

print(verification_number % 10)