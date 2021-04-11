/* 나의 풀이 (Multiple Pointers Pattern 사용 X) */
function myCountUniqueValues(sortedArray) {
  // 1. 빈 배열인 경우 0으로, 그렇지 않은 경우 1로 초기화한다.
  let count = sortedArray.length > 0 ? 1 : 0;

  // 2. 배열을 순회하며, 바로 뒤 원소가 현재 원소와 다르면 카운터를 증가시킨다.
  sortedArray.forEach((elem, index) => {
    if (index > 0) {
      if (elem !== sortedArray[index - 1]) {
        count++;
      }
    }
  });

  // 3. 반환한다.
  return count;
}

/* 나의 풀이 (Multiple Pointers Pattern 사용 O) */
function countUniqueValues(sortedArray) {
  // 1. 포인터 두개를 선언한다.
  let i = 0;
  let j = 0;

  // 2. 포인터 j를 이동하면서, 포인터 i가 가리키는 값과 비교한다.
  while(j < sortedArray.length) {
    // 2-1. 두 값이 다른 경우, i를 1만큼 증가시키고 j의 값으로 바꾼다. 
    if (sortedArray[i] !== sortedArray[j]) {
      sortedArray[++i] = sortedArray[j];
    }
    // 2-2. 두 값이 같은 경우, j를 1만큼 증가시킨다.
    else {
      j++;
    }
  }

  // 3. 포인터 i의 값을 반환한다.
  return i > 0 ? i + 1 : i;
}

console.log(countUniqueValues([1, 1, 1, 2])); // 2
console.log(countUniqueValues([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13])); // 7
console.log(countUniqueValues([])); // 0
console.log(countUniqueValues([-2, -1, -1, 0, 1])); // 4
