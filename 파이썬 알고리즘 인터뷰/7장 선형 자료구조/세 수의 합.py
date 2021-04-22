class Solution:
    # 나의 브루트포스를 이용한 풀이 (Time Limit Exceeded)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sorted_array = sorted([nums[i], nums[j], nums[k]])
                        
                        if sorted_array not in answer:
                            answer.append(sorted_array)
        
        return answer

    # 나의 투포인터를 이용한 풀이(Runtime: 4732ms, Memory: 17.5MB)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        # 배열을 정렬해 투 포인터를 사용할 수 있도록 한다.
        nums.sort()
        
        for idx in range(0, len(nums)):
          left = idx + 1
          right = len(nums) - 1
          
          # 투 포인터가 만날 때까지 반복한다.
          while left < right:
              temp = nums[idx] + nums[left] + nums[right]
              
              # 합이 0보다 작은 경우, 왼쪽 포인터만 이동시킨다.
              if temp < 0:
                  left += 1
              # 합이 0보다 큰 경우, 오른쪽 포인터만 이동시킨다.
              elif temp > 0:
                  right -= 1
              # 합이 0인 경우, answer 배열에 추가하고 양측 포인터를 모두 이동시킨다.
              else:
                  if [nums[idx], nums[left], nums[right]] not in answer:
                      answer.append([nums[idx], nums[left], nums[right]])
                  left += 1
                  right -= 1
                      
        return answer