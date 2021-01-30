# 8980 : 택배
#
# 택배를 빨리 보내는 순서대로 오름차순 정렬하고 트럭을 최소힙으로 구현해 풀이하려고 했으나, 계속 오답이 나와서 답지를 확인했다.
#
# 트럭이 운반할 수 있는 무게로 초기화된 (마을 개수 + 1)길이의 배열을 만든다.
# "빨리 도착하는 순서대로" 정렬된 택배들을 순서대로 조회하면서 해당 택배가 이동해야 하는 시작/도착지 사이에 남은 운반 가능 무게를 확인한다.
# 운반 가능 무게가 남은 경우, 해당 택배만큼 운송 범위 내의 마을에 대해 운송 가능 무게에서 택배 무게를 뺀다.
# 만약 (운반 가능 무게 - 택배 무게) < 0 이라면, 운반 가능 무게만 뺀다.


N, C = map(int, input().split())
M = int(input())
deliveries = []

for _ in range(M):
    origin, dest, weight = map(int, input().split())
    deliveries.append([origin, dest, weight])

deliveries.sort(key=lambda elem: elem[1])

village = [C] * (N + 1)
delivered = 0

for idx in range(M):
    origin, dest, weight = deliveries[idx]
    max_weight = min(village[origin: dest])

    if max_weight == 0:
        continue

    if weight <= max_weight:
        for visited in range(origin, dest):
            village[visited] -= weight
        delivered += weight
    else:
        for visited in range(origin, dest):
            village[visited] -= max_weight
        delivered += max_weight

print(delivered)
