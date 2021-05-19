import math

num_a, num_b = map(int, input().split())
gcd = math.gcd(num_a, num_b)

print(gcd)
print((num_a * num_b) // gcd)  # 최소공배수
