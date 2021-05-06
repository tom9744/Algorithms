from typing import List


class Solution:
    # 이진 검색 풀이 (Runtime: 52ms, Memory: 14.2MB)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums2.sort()

        # 두번째 배열에서 이진 검색을 통해 첫번째 배열의 원소를 찾는다.
        for num in nums1:
            left, right = 0, len(nums2) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums2[mid] < num:
                    left = mid + 1
                elif num < nums2[mid]:
                    right = mid - 1
                # 일치하는 값이 있는 경우, 집합(Set)에 추가한다.
                else:
                    result.add(num)
                    break

        return list(result)

    # 브루트포스 풀이 (Runtime: 128ms, Memory: 14.2MB)
    def intersection_bruteforce(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()

        # 두 배열에 모두 존재하는 원소를 집합(Set)에 추가한다.
        for x in nums1:
            for y in nums2:
                if x == y:
                    result.add(x)

        return list(result)
