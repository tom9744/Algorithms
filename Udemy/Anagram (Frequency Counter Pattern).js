/* 나의 풀이 */
function validAnagram(strA, strB) {
  // 1. 문자열의 길이를 체크한다.
  if (strA.length !== strB.length) {
    return false;
  }

  const counterA = frequencyCounter(strA);
  const counterB = frequencyCounter(strB);

  // 3. 빈도수 체크 결과를 비교한다.
  for(const key in counterA) {
    const count = counterA[key];

    // 3-1. 해당 문자가 존재하지 않으면 Anagram이 아니다.
    if (!counterB[key]) {
      return false;
    }

    // 3-2. 해당 문자가 존재하더라도, 빈도수가 다르면 Anagram이 아니다.
    if (count !== counterB[key]) {
      return false;
    }
  }

  // 4. 결과를 반환한다.
  return true;
}

function frequencyCounter(str) {
  const counter = {};

  // 2. 문자열을 구성하는 문자를 하나씩 체크해, 등장하는 빈도수를 센다.
  for(const char of str) {
    counter[char] 
      ? counter[char]++     // 2-1. 카운터 객체의 key가 이미 존재하면 value를 1만큼 증가.
      : counter[char] = 1;  // 2-2. 카운터 객체의 key가 존재하지 않으면, 1로 초기화.
  }

  return counter;
}


console.log(validAnagram("aaz", "zza"));          // false
console.log(validAnagram("anagram", "nagaram"));  // true
console.log(validAnagram("qwerty", "qeywrt"));    // true