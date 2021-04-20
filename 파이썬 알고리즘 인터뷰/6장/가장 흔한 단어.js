// 나의 풀이 (Runtime: 88ms, Memory: 40.2MB)
const mostCommonWord = function(paragraph, banned) {
  // filter, reduce를 이용해 불필요한 공백과 금지어를 제거하고, 빈도수를 계산한다.
  const frequency = paragraph.toLowerCase().replace(/[^a-zA-Z]/g, " ").split(" ")
    .filter(word => !(banned.includes(word) || word === ""))
    .reduce((counter, word) => {
      counter[word] = counter[word] ? counter[word] + 1 : 1;
      return counter;
    }, {});

  // 가장 많이 등장한 단어를 찾는다.
  let max = -Infinity;
  let answer;

  for (const key in frequency) {
    if (frequency[key] > max) {
      max = frequency[key];
      answer = key;
    }
  }

  return answer;
};