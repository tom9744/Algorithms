import heapq

from typing import List
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프를 구성한다.
        graph = defaultdict(list)
        for start_vertex, dest_vertex, time in times:
            graph[start_vertex].append((dest_vertex, time))

        priority_queue = [(0, k)]  # 우선순위 큐
        distance = defaultdict(int)  # 시작점에서 각 노드까지의 최단 거리를 저장하기 위한 딕셔너리

        while priority_queue:
            # 현 시점에서 가장 비용이 적은 정점을 고른다.
            time, vertex = heapq.heappop(priority_queue)

            # 현 정점이 최단 거리 딕셔너리에 존재하지 않는 경우,
            if not vertex in distance:
                # 최단 거리 딕셔너리에 추가한다.
                distance[vertex] = time
                # 인접한 정점까지의 거리를 구하고, 우선순위 큐에 삽입한다.
                for adj_vertex, next_time in graph[vertex]:
                    total_time = time + next_time
                    heapq.heappush(priority_queue, (total_time, adj_vertex))

        # 모든 정점까지의 거리를 구할 수 없는 경우, -1을 반환한다.
        if len(distance) == n:
            return max(distance.values())
        return -1
