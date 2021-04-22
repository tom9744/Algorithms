class Solution:
    # 나의 풀이 (Runtime: 36ms, Memory: 14.5MB)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        # 해시 테이블을 구성한다.
        for idx, num in enumerate(nums):
            hash_map[num] = idx
            
        for idx, num in enumerate(nums):
            num_to_find = target - num
            
            # 목표 값에서 첫번째 값을 뺀 결과 값을 Key로 사용, 중복 사용 제외.
            if num_to_find in hash_map and idx != hash_map[num_to_find]:
                return [idx, hash_map[num_to_find]]