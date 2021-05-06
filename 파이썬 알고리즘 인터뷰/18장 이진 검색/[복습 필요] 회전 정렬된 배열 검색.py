from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))  # 가장 작은 값을 찾아, 회전된 pivot 값을 구한다.

        left, right = 0, len(nums) - 1

        while left <= right:
            # [0,1,2,4,5,6,7]가 [4,5,6,7,0,1,2]로 회전된 상황을 고려해, 이진 검색을 수행한다.
            mid = left + (right - left) // 2
            rotated_mid = (mid + pivot) % len(nums)  # 회전된 중앙값의 인덱스

            if nums[rotated_mid] < target:
                left = mid + 1
            elif nums[rotated_mid] > target:
                right = mid - 1
            else:
                return rotated_mid

        return -1