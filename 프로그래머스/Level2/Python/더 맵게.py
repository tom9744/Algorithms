# 코딩테스트 연습 > 힙(Heap) > 더 맵게 (Level2)
import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville[0] < K:
        # 더 이상 새로운 음식을 만들 수 없지만, K값에 도달하지 못한 경우 -1 반환
        if len(scoville) < 2:
            return -1

        least = heapq.heappop(scoville)  # 가장 맵지 않은 음식의 스코빌 지수
        less = heapq.heappop(scoville)  # 두 번째로 맵지 않은 음식의 스코빌 지수

        heapq.heappush(scoville, least + (less * 2))  # 특별한 방법으로 섞어, 새로운 음식 개발

        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
