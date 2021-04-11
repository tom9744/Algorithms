function maxSubarraySum(array, windowSize) {
  // 0. 윈도우 크기가 배멸의 길이보다 크다면, null을 반환한다.
  if (array.length < windowSize) {
    return null;
  }
  
  let maxVal = -Infinity;
  
  // 1. 배열을 왼쪽부터 오른쪽으로 순회하며, 인자로 주어진 윈도우의 크기만큼 자른다.
  for (let index = 0; index < array.length - windowSize + 1; index++) {
    const window = array.slice(index, index + windowSize);

    // 2. 윈도우 크기에 해당하는 요소들의 합을 구한다.
    const subarraySum = window.reduce((acc, curr) => acc + curr, 0);

    // 3. 현재 최대값과 비교 후, 더 크다면 교체한다.
    if (maxVal < subarraySum) {
      maxVal = subarraySum;
    }
  }

  return maxVal;
}

maxSubarraySum([2, 6, 3, 2, 1, 2, 4], 3); // 11