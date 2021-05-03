import heapq

from typing import List
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # 그래프를 생성한다.
        graph = defaultdict(list)
        for departure, arrival, price in flights:
            graph[departure].append((arrival, price))

        # 우선순위 큐를 초기화한다.
        p_queue = [(0, src, K)]

        # BFS, Dijkstra
        while p_queue:
            current_price, current_city, k = heapq.heappop(p_queue)

            # 목적지에 도달한 경우, 현재까지의 비용을 반환한다.
            if current_city == dst:
                return current_price

                # K 경유지 이내인 이웃 정점만 조회한다.
            if k >= 0:
                for city, price in graph[current_city]:
                    next_price = current_price + price
                    heapq.heappush(p_queue, (next_price, city, k - 1))

        # 목적지에 도달하지 못한 경우, -1을 반환한다.
        return -1
