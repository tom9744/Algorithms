A, B = map(int, input().split())
AB = A * B

if A < B:
    A, B = B, A  # Swap

# 유클리드 호제법
while B > 0:
    remainder = A % B
    A = B
    B = remainder

print(A)
print(AB // A)
