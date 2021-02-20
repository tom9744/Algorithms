# 1463 : 1로 만들기
#
# 가장 기본적인 Bottom-Up 방식의 DP 문제라고 한다.
#
# 최소 숫자부터 시작해서 해당 숫자를 만들 수 있는 연산의 최소 횟수를 구하고, 배열에 저장해 기억한다.
# 이후부터는 처음부터 다시 구하는 것이 아니라, DP[num] = DP[num - 1] + 1과 같은 방식으로 이전에 구한 값을 사용한다.
#
# 문제의 경우, 사용할 수 있는 연산의 개수가 3개이므로, 세 가지 연산을 적용한 경우 중 최소값을 DP[num]에 저장하면 된다.

N = int(input())
DP = [0 for _ in range(N + 1)]

for num in range(1, N + 1):
    if num == 1:
        DP[num] = 0
        continue

    DP[num] = DP[num - 1] + 1

    if num % 2 == 0 and DP[num // 2] + 1 < DP[num]:
        DP[num] = DP[num // 2] + 1

    if num % 3 == 0 and DP[num // 3] + 1 < DP[num]:
        DP[num] = DP[num // 3] + 1

print(DP[N])
