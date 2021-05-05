import heapq

from typing import List


class Solution:
    def myAnswer(self, nums: List[int], k: int) -> int:
        p_queue = []

        # 음수 값으로 변환해 최대 힙을 구현한다.
        for num in nums:
            heapq.heappush(p_queue, -num)

        for _ in range(k - 1):
            heapq.heappop(p_queue)

        return -heapq.heappop(p_queue)

    """
    heapq 모듈의 nlargest() 메서드는 n번째 큰 원소로 구성된 배열을 반환한다.
    (ex) heapq.nlargest(2, [1, 2, 3, 4, 5, 6]) -> [6, 5]
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
