# 2609: 최대공약수와 최소공배수
#
# 유클리드 호제법 (나머지 연산)을 이용해 최대공약수를 계산하며,
# LCM(A, B) = (A * B) / GCD(A, B) 식을 이용해 최소공배수를 구한다.

X, Y = map(int, input().split())
multiply = X * Y

if X < Y:
    temp = X
    X = Y
    Y = temp

# 유클리드 호제법
#
# GCD(A, B) = GCD(B, A % B)
# if A % B == 0, then GCD = B
# else GCD(B, A % B)
while X % Y != 0:
    remainder = X % Y
    X = Y
    Y = remainder

print(Y)
print(multiply // Y)
