# 2747 : 피보나치
#
# 처음엔 재귀 함수로 접근했지만, 시간 초과가 나왔다.
# 따라서 주어진 N 번째 피보나치수를 구하는 반복문 구현해 풀이하였다.

N = int(input())
fibonacci = [0, 1, ]

for n in range(2, N + 1):
    fibonacci.append(fibonacci[n - 1] + fibonacci[n - 2])

if N == 0:
    print(1)
else:
    print(fibonacci.pop())


# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 2) + fibonacci(n - 1)
#
#
# N = int(input())
#
# print(fibonacci(N))
