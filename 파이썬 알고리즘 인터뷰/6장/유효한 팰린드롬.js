/**
 * @param {string} s
 * @return {boolean}
 */
const isPalindrome = function(str) {
  // 문자열을 소문자로 변환하고, 정규식에 일치하지 않는 문자는 제외한다.
  const regEx = /[0-9a-z]/;
  const filteredStr = str.toLowerCase().split("").filter(char => char.match(regEx));

  let leftIdx = 0;
  let rightIdx = filteredStr.length - 1;

  // 배열의 양측에서 포인터를 가운데로 이동시키며, 동일한 문자인지 확인한다.
  while (leftIdx < rightIdx) {
    if (filteredStr[leftIdx] !== filteredStr[rightIdx]) {
      return false;
    }

    leftIdx++;
    rightIdx--;
  }

  return true;
};