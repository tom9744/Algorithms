# 1932 : 정수 삼각형
#
# 주어지는 삼각형과 똑같은 크기의 삼각형 배열을 선언하고, 꼭지점부터 한 층씩 내려오면서
# 가능한 값들의 최대값을 DP 배열에 저장한다.
#
# 각 층의 맨 왼쪽과 오른쪽은 위층의 값을 그대로 가져오며, 중앙값은 위 층의 대각선 방향 값 중 더 큰 값을 선택한다.
# DP[i].append(max(DP[i - 1][j - 1], DP[i - 1][j]) + triangle[i][j])
#
# 마지막 층에 누적된 값들 중 최대값을 출력하면 정답이다.


N = int(input())
triangle = [[] for _ in range(N)]
DP = [[] for _ in range(N)]

for index in range(N):
    triangle[index] = list(map(int, input().split()))

for i in range(N):
    if i == 0:
        DP[i] = triangle[i]
    else:
        length = len(triangle[i])

        for j in range(length):
            if j == 0:
                DP[i].append(DP[i - 1][0] + triangle[i][j])
            elif j == length - 1:
                DP[i].append(DP[i - 1][length - 2] + triangle[i][j])
            else:
                DP[i].append(max(DP[i - 1][j - 1], DP[i - 1][j]) + triangle[i][j])

print(max(DP[N - 1]))