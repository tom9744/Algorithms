class Solution:
    # 나의 풀이 (Runtime: 288ms, Memory: 16.9MB)
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        summary = 0
        
        for idx in range(0, len(nums) - 1, 2):
            summary += min(nums[idx], nums[idx + 1])

        return summary

    # 책의 인덱스 특성을 이용한 풀이 (Runtime: 276ms, Memory: 16.9MB)
    def answer_without_min(self, nums: List[int]) -> int:
        nums.sort()
        summary = 0

        # 정렬된 경우, 짝수 인덱스의 값이 항상 짝(Pair)의 최소값이다.  
        for idx in range(0, len(nums) - 1, 2):
            summary += nums[idx]

        return summary
    