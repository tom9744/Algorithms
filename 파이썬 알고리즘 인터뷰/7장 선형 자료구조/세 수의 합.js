// 나의 투포인터를 이용한 풀이(Runtime: 468ms, Memory: 52.3MB)
const threeSum = function(nums) {
  const sorted = nums.sort((numA, numB) => numA - numB);
  const answer = {};
  
  for (let idx = 0; idx < nums.length; idx++) {
    let left = idx + 1;
    let right = nums.length - 1;
    
    // [참고] outOfRange는 아래 조건만으로 예외처리된다.
    while(left < right) {
      const result = nums[idx] + nums[left] + nums[right];
      
      if (result < 0) {
        left++;
      } else if (result > 0) {
        right--;
      } else {
        // 중복 처리를 위해 숫자를 문자열로 변환해 더한 값을 Key로 사용한다.
        const tripet = [nums[idx], nums[left], nums[right]]; 
        const key = tripet.reduce((str, num) => str + num, "");
        
        answer[key] = tripet;
        left++;
        right--;
      }
    }
  }
   
  return Object.values(answer);
};