// 나의 풀이 (Runtime: 92ms, Memory: 41.3MB)
const expand = (string, left, right) => {
  // left와 right가 범위 내에 있을 때, 양쪽으로 확장하며 팰린드롬 여부를 검사한다.
  while (left >= 0 && right < string.length) {
    if (string[left] !== string[right]) {
      break;
    }

    left--;
    right++;
  }

  // 증감 연산자가 반복문 종료 시 한번 더 계산되므로,  left + 1 해준다. 
  return string.slice(left + 1, right);
}

const longestPalindrome = function(str) {
  // 길이가 1이거나, 문자열 전체가 팰린드롬인 경우 즉시 반환한다.
  if (str.length < 2 || str === str.split("").reverse().join("")) {
    return str;
  }

  let result = "";

  // 짝수, 홀수에 대한 투 포인터 각각을 이동시키며 확인한다.
  for (let idx = 0; idx < str.length; idx++) {
    const evenPalindrome = expand(str, idx, idx + 1); // 2 -> 4 -> 6
    const oddPalindrome = expand(str, idx, idx + 2);  // 3 -> 5 -> 7

    result = evenPalindrome.length > result.length ? evenPalindrome : result;
    result = oddPalindrome.length > result.length ? oddPalindrome : result;
  }

  return result;
};
