function signFunc(product) {
  return product === 0 
    ? 0 
    : product > 0 ? 1 : -1;
}

/**
 * @param {number[]} nums
 * @return {number}
 */
const arraySign = function(nums) {
  // 매번 signFunc()를 호출해 숫자가 초과되지 않도록 한다.
  return nums.reduce((accumulator, current) => signFunc(accumulator * current), 1);
};