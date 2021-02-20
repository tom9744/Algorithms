# 10870 : 피보나치 수 5
#
# 피보나치 수를 재귀함수를 이용해 구하면, 4번째 피보나치 수를 구하기 위해
# 3번째 피보나치 수는 한 번, 2번째 피보나치 수는 두 번, 1번째 피보나치 수는 세 번, 0번째 피보나치 수는 두 번 구해야 한다.
#
# 이럴 때 "동적 계획법"을 사용해 "이미 한번 구한 값은 다시 계산하지 않는" 전략을 사용하면
# 연산량을 획기적으로 줄일 수 있다

N = int(input())

if N == 0:
    print(0)
else:
    DP = [0 for _ in range(N + 1)]
    DP[0], DP[1] = 0, 1

    for number in range(2, N + 1):
        DP[number] = DP[number - 1] + DP[number - 2]

    print(DP[N])
