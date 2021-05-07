from typing import List

import collections


class Solution:
    # 브루트 포스 풀이 (시간초과)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        result = []

        for left in range(len(nums) - k + 1):
            result.append(max(nums[left:left + k]))

        return result

    # 큐를 이용한 최적화 (시간초과)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = collections.deque()
        current_max = float('-inf')

        for idx, num in enumerate(nums):
            window.append(num)
            if idx < k - 1:
                continue

            if current_max == float('-inf'):
                current_max = max(window)
            elif num > current_max:
                current_max = num

            result.append(current_max)

            popped = window.popleft()
            if popped == current_max:
                current_max = float('-inf')

        return result