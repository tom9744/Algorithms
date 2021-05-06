from typing import List


class Solution:
    # 투 포인터 풀이 (Runtime: 92ms, Memory: 14.8MB)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for idx, num in enumerate(numbers):
            # 중복하여 사용할 수 없으므로, 자기자신을 제외하고 탐색한다.
            left, right = idx + 1, len(numbers) - 1
            expected = target - num

            # 이진 검색을 수행한다.
            while left <= right:
                mid = left + (right - left) // 2

                if numbers[mid] < expected:
                    left = mid + 1
                elif expected < numbers[mid]:
                    right = mid - 1
                else:
                    # 1-indexed 규칙에 따라, 각 인덱스에 1을 더해 반환한다.
                    return [idx + 1, mid + 1]

        return []

    # 투 포인터 풀이 (Runtime: 64ms, Memory: 14.8MB)
    def twoSum_two_pointers(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        # 양쪽에서 포인터를 중앙으로 옮기며 일치하는 값이 있는지 탐색한다.
        while left < right:
            current = numbers[left] + numbers[right]

            if current < target:
                left += 1
            elif target < current:
                right -= 1
            else:
                # 1-indexed 규칙에 따라, 각 인덱스에 1을 더해 반환한다.
                return [left + 1, right + 1]
