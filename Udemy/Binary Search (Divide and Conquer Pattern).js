/* Time Complexity of O(N) */
function linearSearch(array, target) {
  let foundElemIndex = -1;
  
  for (let index = 0; index < array.length; index++) {
    if (array[index] === target) {
      foundElemIndex = index;
      break;
    }
  }

  return foundElemIndex;
}

console.log(linearSearch([1, 2, 3, 4, 5, 6, 7, 8], 5));  // 4
console.log(linearSearch([1, 2, 3, 4, 5, 6, 7, 8], 9));  // -1

/* Time Complexity of O(logN) */
function binarySearch(array, target) {
  let tempArray = array.sort((numA, numB) => numA - numB);

  while (tempArray.length > 0) {
    const middleIndex = Math.floor(tempArray.length / 2);
  
    // 배열의 중간값이 찾고자하는 값보다 큰 경우, 배열의 왼쪽 절반을 취한다.
    if (tempArray[middleIndex] > target) {
      tempArray = tempArray.slice(0, middleIndex);
    }
    // 배열의 중간값이 찾고자하는 값보다 작은 경우, 배열의 오른쪽 절반을 취한다.
    else if (tempArray[middleIndex] < target) {
      tempArray = tempArray.slice(middleIndex + 1);
    }
    // 배열의 중간값이 찾고자하는 값과 일치하는 경우, 해당 인덱스를 반환한다.
    else {
      return middleIndex;
    }
  }

  return -1;
}

console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 5));  // 4
console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 9));  // -1

