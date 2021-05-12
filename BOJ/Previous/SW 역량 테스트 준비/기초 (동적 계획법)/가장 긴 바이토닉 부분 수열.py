# 11054: 가장 긴 바이토닉 부분 수열
#
# [11053: 가장 긴 증가하는 부분 수열] 문제의 응용 문제로,
# 순열의 양 끝 지점에서 시작해 현재 숫자까지 증가하는 순열의 길이를 구하면 된다.
#
# DP 배열의 경우, 왼쪽에서 계산한 증가 순열의 길이와 오른쪽에서 계산한 증가 순열의 길이
# 두 가지를 모두 저장할 수 있도록 2차원 배열로 정의해야 한다.
#
# 또한 시간이 1초 밖에 주어지지 않았으므로 중복 연산을 수행하면 안되고, 배열 인덱스를 이용해야 한다
#
# 마지막으로 DP 배열 중 왼쪽/오른쪽에서 계산한 증가 수열의 길이 합이 최대값인 것을 출력한다.
# 이때, -1을 해주어야 정상적인 정답이 도출된다.

N = int(input())
DP = [[1, 1] for _ in range(N)]
permutation = list(map(int, input().split()))

for curr in range(N):
    for num in range(curr):
        if permutation[num] < permutation[curr]:
            DP[curr][0] = max(DP[curr][0], DP[num][0] + 1)
        if permutation[N - curr - 1] > permutation[N - num - 1]:
            DP[N - curr - 1][1] = max(DP[N - curr - 1][1], DP[N - num - 1][1] + 1)

max_value = 0
for each in DP:
    total = each[0] + each[1] - 1
    if max_value < total:
        max_value = total

print(max_value)

