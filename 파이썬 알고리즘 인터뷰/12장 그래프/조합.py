class Solution:
    # 직접 구현한 풀이 (Runtime: 440ms, Memory: 15.8MB)
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
    
        def dfs(numbers, start, k):
            if k == 0:
                result.append(numbers[:])
                return
            
            # 자기 자신 이후의 모든 수에 대해 재귀 호출.
            for idx in range(start, n + 1):
                numbers.append(idx)
                dfs(numbers, idx + 1, k - 1)
                numbers.pop()  # 백트래킹
        
        dfs([], 1, k)
        
        return result
    
    # itertools를 사용한 풀이 (Runtime: 68ms, Memory: 15MB)
    def combine(self, n: int, k: int) -> List[List[int]]:
        return itertools.combinations([i for i in range(1, n + 1)], k)