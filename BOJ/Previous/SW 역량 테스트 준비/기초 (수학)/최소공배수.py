# 1934: 최소공배수

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    mul = A * B

    if A < B:
        temp = A
        A = B
        B = temp

    while A % B != 0:
        remainder = A % B
        A = B
        B = remainder

    GCD = B
    LCM = mul // GCD

    print(LCM)
    