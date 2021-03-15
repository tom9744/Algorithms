# 가장 긴 증가하는 부분 수열 4
#
# [[1, [numbers[i], ]] for i in range(N)]와 같이 DP 배열을 초기화할 때
# 순열을 담을 배열에 자기자신을 추가해 놓으면, 별도 조건 처리를 안해주고 풀이할 수 있다.
#
# 초기화하지 않을 경우, 10 20 50 60 30 40 50 같은 경우에서 오답처리 된다.

N = int(input())
numbers = list(map(int, input().split()))

DP = [[1, [numbers[i], ]] for i in range(N)]

for curr in range(N):
    for num in range(curr):
        # 현재 숫자보다 작은 숫자에 대해,
        if numbers[num] < numbers[curr]:
            # 2차원 DP 배열 중, 수열의 길이를 나타내는 첫번째 원소를 비교한다.
            # 이전 길이 + 1 > 현재 길이이면, DP 배열을 갱신한다.
            if DP[num][0] + 1 > DP[curr][0]:
                DP[curr][0] = DP[num][0] + 1  # 수열의 길이 + 1
                DP[curr][1] = DP[num][1].copy()  # 이전 숫자까지 누적된 수열 배열 복사
                DP[curr][1].append(numbers[curr])  # 복사한 배열에 이번 숫자 추가

result = max(DP)
print(result[0])
for elem in result[1]:
    print(elem, end=" ")