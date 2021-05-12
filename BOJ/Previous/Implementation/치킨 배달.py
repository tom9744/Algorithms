# 15686 : 치킨 배달
#
# 배열의 전체 원소 중 M개를 선택해 만들 수 있는 모든 조합을 만들어주는 라이브러리 'itertools.combinations'를 사용해야 한다.
# 이렇게 생성된 M개의 치킨집 조합에 대해 '도시의 치킨 거리'를 계산한다. (= 각 집에서 제일 가까운 치킨집까지의 거리 합)
#
# 모든 치킨집 조합으로 구한 '도시의 치킨 거리' 중 최소값을 출력하면 된다.

import sys, itertools

N, M = map(int, sys.stdin.readline().rstrip().split())
houses = []
chickens = []
for r in range(1, N + 1):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    c = 0
    for each in row:
        c += 1
        if each == 1:
            houses.append((r, c))
        elif each == 2:
            chickens.append((r, c))

possible_distances = []

for combination in itertools.combinations(chickens, M):
    distances = []
    for house in houses:
        minimum = 100
        house_r, house_c = house

        for chicken in combination:
            chicken_r, chicken_c = chicken

            distance = abs(chicken_r - house_r) + abs(chicken_c - house_c)

            if distance < minimum:
                minimum = distance

        distances.append(minimum)

    possible_distances.append(sum(distances))

print(min(possible_distances))

