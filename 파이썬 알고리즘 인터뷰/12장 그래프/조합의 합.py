class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(summary, start, path):
            # target이 0, 또는 0보다 작아지면 함수를 종료한다.
            if summary == 0:
                result.append(path[:])
                return
            if summary < 0:
                return
            
            # 중복 조합을 탐색하며, target에서 현재 값을 빼고 재귀 호출한다.
            for idx in range(start, len(candidates)):
                dfs(summary - candidates[idx], idx, path + [candidates[idx]])
            
        dfs(target, 0, [])
        
        return result