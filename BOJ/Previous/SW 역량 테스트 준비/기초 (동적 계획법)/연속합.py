# 1912: 연속합
#
# DP[N - 1] + number[N]의 결과가 number[N]보다 작은 경우,
# DP[N]에 number[N]의 값을 그대로 집어 넣는다.
# 그 외의 경우에는 DP[N - 1] + number[N]의 값을 집어 넣는다.
#
# DP 배열에서 최대값을 출력하면 정답이다.

n = int(input())
numbers = list(map(int, input().split()))
DP = [0 for _ in range(n)]

for num in range(n):
    if num < 1:
        DP[num] = numbers[num]
    else:
        DP[num] = max(numbers[num], DP[num - 1] + numbers[num])

print(max(DP))