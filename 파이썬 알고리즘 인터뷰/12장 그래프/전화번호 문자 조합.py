class Solution:
    # 책의 풀이 (Runtime: 32ms, Memory: 14.4MB)
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        result = []
        keys = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        def dfs(index=0, path=""):
            # [NOTE] digits 길이만큼 path가 생성되지 않으면 함수가 종료된다.
            if len(digits) == len(path):
                result.append(path)
                return
        
            # [EXAMPLE] idx가 1일 때, { '3': 'def' }에 대해 반복문이 실행되지만,
            # 다음 idx가 2가 되어서 반복문이 실행되지 않고 함수가 종료된다. 
            for idx in range(index, len(digits)):
                for char in keys[digits[idx]]:
                    dfs(idx + 1, path + char)
                    
        dfs()
        
        return result