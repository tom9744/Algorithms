import bisect

from typing import List


class Solution:
    # 이진 검색을 직접 구현한 풀이 (Runtime: 240ms, Memory: 23MB)
    def search_recursive(self, nums: List[int], target: int) -> int:
        def binary_search(low, high):
            if low <= high:
                mid = low + (high - low) // 2

                # 중앙값이 목표값보다 작은 경우, 중앙값의 오른쪽에 대해 이진 검색 재귀 호출
                if nums[mid] < target:
                    return binary_search(mid + 1, high)
                # 중앙값이 목표값보다 큰 경우, 중앙값의 왼쪽에 대해 이진 검색 재귀 호출
                elif nums[mid] > target:
                    return binary_search(low, mid - 1)
                # 중앙값괴 목표값이 일치하는 경우, 중앙값의 인덱스를 반환
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)

    # 모듈을 사용한 풀이 (Runtime: 224ms, Memory: 15.6MB)
    def search_module(self, nums: List[int], target: int) -> int:
        # bisect_left() 메서드는 target 값을 삽입할 위치를 반환한다.
        index = bisect.bisect_left(nums, target)

        # 따라서 index 값이 배열 범위 내에 있는지, target 값과 일치하는지 확인해야 한다.
        return index if index < len(nums) and nums[index] == target else -1