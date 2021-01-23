# 2217 : 로프
#
# 로프의 무게 한도를 모은 배열을 역순으로 정렬한 뒤,
# 한도가 높은 로프부터 사용해보며 최대값을 찾는다.

num_of_ropes = int(input())
limits = []

for _ in range(num_of_ropes):
    limits.append(int(input()))

limits.sort(reverse=True)

maximum = limits[0]
current = 0

for index in range(1, len(limits)):

    current = limits[index] * (index + 1)
    if current > maximum:
        maximum = current

print(maximum)