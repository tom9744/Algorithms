// 브루트포스를 이용한 풀이 (Runtime: 72ms, Memory: 38.6MB)
const twoSumBruteForce = function(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  } 
};

// Object 기반의 Hash를 이용한 풀이 (Runtime: 84ms, Memory: 41.3MB)
 const twoSumHashMap = function(nums, target) {
  // reduce()를 이용해 해시테이블을 생성한다.
  const hashMap = nums.reduce((hash, num, idx) => {
    hash[num] = idx;
    return hash;
  }, {});

  for (let idx = 0; idx < nums.length; idx++) {
    const numToFind = target - nums[idx];
    
    // 목표 값에서 첫번째 값을 뺀 값을 Key로 이용해 Hash를 조회한다.
    if (hashMap.hasOwnProperty(numToFind) && idx !== hashMap[numToFind]) {
      return [idx, hashMap[numToFind]];
    }
  }
};