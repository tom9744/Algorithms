class Solution:
    # 직접 구현한 풀이 (Runtime: 40ms, Memory: 14.5MB)
    def permute(self, nums: List[int]) -> List[List[int]]:
    permutation = []
    result = []
    
    def dfs(numbers):
        if not numbers:
            # 객체의 참조 대신 배열 복사본을 추가해야 한다.
            result.append(permutation[:])
            return
    
        for number in numbers:
            next_numbers = numbers[:]
            next_numbers.remove(number)
            
            permutation.append(number)
            dfs(next_numbers)
            # [백트래킹] dfs()가 완료되면 배열에서 원소를 하나씩 제거한다.
            # 예를 들어, [1, 2, 3]을 완성한 뒤 [1]로 돌아간다.
            permutation.pop()  
            
        dfs(nums)
    
        return result
    
    # itertools를 사용한 풀이 (Runtime: 32ms, Memory: 14.3MB)
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums, len(nums))