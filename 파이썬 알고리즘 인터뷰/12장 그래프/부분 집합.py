class Solution:
    # 나의 풀이 (Runtime: 24ms, Memory: 14.4MB)
    def subsets(self, nums: List[int]) -> List[List[int]]: 
        result = []
        
        def dfs(start_index, subset):
            result.append(subset)
            
            # 경로를 생성하며 DFS를 재귀호출한다.
            for idx in range(start_index, len(nums)):
                dfs(idx + 1, subset + [nums[idx]])        
                
        dfs(0, [])
        
        return result