from typing import List

import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        p_queue = []
        for person in people:
            heapq.heappush(p_queue, (-person[0], person[1]))

        # 가장 키가 큰 사람부터 꺼내고, 앞에 있는 사람 수에 해당하는 인덱스에 삽입한다.
        # (ex) [7, 1]은 배열의 인덱스 1 위치에 삽입한다.
        result = []
        while p_queue:
            person = heapq.heappop(p_queue)

            result.insert(person[1], [-person[0], person[1]])

        return result
