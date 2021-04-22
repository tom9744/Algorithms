// 나의 풀이 (Runtime: 136ms, Memory: 44MB)
const arrayPairSum = function(nums) {
  return nums.sort((numA, numB) => numA - numB)
    .reduce((acc, curr, index) => {
      // 짝수 인덱스만 합산한다.
      if (index % 2 === 0) return acc + curr;
      else return acc;
    }, 0);
};