# 11053 : 가장 긴 증가하는 부분 수열
#
# N번째 숫자에 대해 1부터 N-1번째 숫자와 비교하며, N번째 숫자보다 값이 작고 누적된 수열 길이(= DP)가 큰 수가 있는지 검사한다.
# 만약 그러한 수가 존재한다면, N번째 숫자의 누적 수열 길이(= DP)를 갱신한다.
#
# 처음엔 최대값을 찾은 뒤, 그 최대값의 인덱스를 사용하는 방법으로 접근했지만,
# 이렇게하면 같은 값 10, 10이라도 누적된 수열의 길이가 다른 경우 잘못된 정답이 도출된다.
#
# 따라서 sequence[i] > sequence[j] and DP[i] < DP[j]와 같이 조건문을 작성해야 한다.

N = int(input())
sequence = list(map(int, input().split()))
DP = [0 for _ in range(N)]

for i in range(N):

    for j in range(i):
        # 현재 숫자가 이전 숫자보다 큰 경우,
        if sequence[i] > sequence[j] and DP[i] < DP[j]:
            DP[i] = DP[j]

    DP[i] += 1

print(max(DP))
