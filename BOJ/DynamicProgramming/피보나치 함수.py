# 1003 : 피보나치 함수
#
# 귀납적 접근 방법을 통해 N >= 2 일때, fibonacci(0)과 fibonacci(1)이 호출되는 횟수는
# N-1, N-2 일 때 각각이 호출된 횟수를 더한 것과 같다는 것을 알 수 있었다.
#
# 따라서 N = 0, N = 1 일 때 fibonacci(0)과 fibonacci(1)이 호출되는 횟수를 미리 DP 배열에 저장해 놓은 뒤,
# 2보다 큰 N이 입력되는 경우 동적 계획법을 이용해 정수 N-1, N-2일 때 호출된 fibonacci(0)과 fibonacci(1)의 수를 더해 나간다.

T = int(input())

for _ in range(T):

    N = int(input())

    if N == 0:
        print(1, end=" ")
        print(0)
    elif N == 1:
        print(0, end=" ")
        print(1)
    else:
        DP = [[] for _ in range(N + 1)]
        DP[0] = [1, 0]
        DP[1] = [0, 1]

        for number in range(2, N + 1):
            DP[number].append(DP[number - 1][0] + DP[number - 2][0])
            DP[number].append(DP[number - 1][1] + DP[number - 2][1])

        print(DP[N][0], end=" ")
        print(DP[N][1])
