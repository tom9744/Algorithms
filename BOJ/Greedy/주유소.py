# 13305 : 주유소
#
# 최저가를 저장하는 변수를 하나 선언한 뒤, 각 도시의 가격을 비교하며 현재까지 가장 저렴했던 가격을 유지하도록 한다.
# 더 저렴한 가격이 나올 때까지 (현재의 최저가 * 도시 간 거리)를 계산해 총합에 더하면 된다.

cities = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

best_price = 10000000000
total_price = 0

for index in range(len(distances)):
    current_price = prices[index]
    if current_price < best_price:
        best_price = current_price

    total_price += best_price * distances[index]

print(total_price)