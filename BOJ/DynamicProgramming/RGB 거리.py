# 1149 : RGB 거리
#
# R, G, B 색상을 연속적으로 사용할 수 없는 것이 아니라, 이웃과 색상이 같지만 않으면 된다. (앞 집만 고려하면 된다.)
# 또한, 가장 첫번째 집에서 최소값을 선택한다고 반드시 결과도 최소값이 되는것은 아니다.
#
# 따라서 각각의 집을 R, G, B 모든 색상으로 칠하는 비용을 구한 뒤, DP 배열에 저장해야 한다.
# (예시) 현재 집을 R로 칠하는 비용 = 현재의 R 비용 + 앞집의 (G, B)로 색칠하는 비용 중 최소값

N = int(input())
prices = [[] for _ in range(N + 1)]
colored = [[0, 0, 0] for _ in range(N + 1)]

for location in range(N):
    R, G, B = map(int, input().split())
    prices[location + 1] = [R, G, B]

for location in range(1, N + 1):
    if location == 1:
        colored[location] = prices[location]
    else:
        colored[location][0] = prices[location][0] + min(colored[location - 1][1], colored[location - 1][2])
        colored[location][1] = prices[location][1] + min(colored[location - 1][0], colored[location - 1][2])
        colored[location][2] = prices[location][2] + min(colored[location - 1][0], colored[location - 1][1])

print(min(colored[N][0], colored[N][1], colored[N][2]))
