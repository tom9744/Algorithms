# 11053: 가장 긴 증가하는 부분 수열 (스스로 X)
#
# 단순히 뒤에 있는 숫자만 비교하면 안되고,
# 현재 숫자까지 모든 숫자와 비교하는 이중 반복문을 사용해야 한다.
# N이 1000보다 작으므로, O(N^2)의 시간복잡도여도 1초안에 연산 가능하다.
#
# N번째 수까지 증가하는 수열의 최대길이를 구하고, DP 배열에 저장한다


N = int(input())
permutation = list(map(int, input().split()))
DP = [1 for _ in range(N)]

for num in range(1, N):
    for idx in range(num):
        if permutation[idx] < permutation[num]:
            DP[num] = max(DP[num], DP[idx] + 1)

print(DP)