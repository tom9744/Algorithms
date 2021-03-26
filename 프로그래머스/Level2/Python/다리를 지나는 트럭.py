# 코딩테스트 연습 > 스택/큐 > 다리를 지나는 트럭 (Level2)
from collections import deque


def get_total_weight(queue):
    total_weight = 0

    for truck in queue:
        truck_weight = truck[0]
        total_weight += truck_weight

    return total_weight


def solution(bridge_length, weight, truck_weights):
    time_passed = 0
    num_of_trucks = len(truck_weights)

    trucks_passed_bridge = []
    trucks_on_bridge = deque()

    while True:
        # 다리를 다 건넌 트럭의 수가 총 트럭의 수와 일치하면 반복문 종료
        if len(trucks_passed_bridge) == num_of_trucks:
            break

        time_passed += 1

        # 다리를 건너는 중인 트럭이 존재하고, 첫 번째 트럭이 다리의 길이만큼 이동했다면,
        if trucks_on_bridge and trucks_on_bridge[0][1] + bridge_length == time_passed:
            first_truck = trucks_on_bridge.popleft()
            trucks_passed_bridge.append(first_truck[0])

        current_total_weight = get_total_weight(trucks_on_bridge)  # 다리를 건너는 중인 트럭들의 무게 합을 구한다.

        # 대기 중인 트럭이 존재하고, 다리에 맨 앞의 트럭이 더 올라갈 수 있다면,
        if truck_weights and current_total_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            trucks_on_bridge.append((truck, time_passed))

    return time_passed


print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110
