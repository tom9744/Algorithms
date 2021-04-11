/* 나의 풀이 (Sliding Window 사용 X) - O(N^2) */
function myMaxSubarraySum(array, windowSize) {
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

/* 답안 풀이 (Sliding Window 사용) - O(N) */
function maxSubarraySum(array, windowSize) {
  // 0. 윈도우 크기가 배멸의 길이보다 크다면, null을 반환한다.
  if (array.length < windowSize) {
    return null;
  }

  // 1. 윈도우에 가장 먼저 포함된 요소들의 합을 구한다.
  let maxSum = array.slice(0, windowSize).reduce((acc, curr) => acc + curr, 0);
  let tempSum = maxSum;

  // 2. 윈도우의 맨앞, 맨뒤 요소만 바꿔가면서 요소들의 합을 구한다.
  for (let index = windowSize; index < array.length; index++) {
    const prev = array[index - windowSize];
    const next = array[index];
    tempSum = tempSum - prev + next;

    maxSum = Math.max(maxSum, tempSum);
  }

  return maxSum;
}

maxSubarraySum([2, 6, 3, 2, 1, 2, 4], 3); // 11