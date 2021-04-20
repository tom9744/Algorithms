// 나의 풀이 (Runtime: 132ms, Memory: 50.5MB)
const groupAnagrams = function(strings) {
  const frequency = {};

  // 각 단어를 배열로 쪼갠 뒤 정렬하여, 애너그램인 경우 동일한 단어로 만든다.
  strings.forEach(string => {
    const key = string.split("").sort().join("");

    // 정렬된 단어를 Key로 사용해, 애너그램을 모은다.
    if (!frequency[key]) {
      frequency[key] = [];
    }

    frequency[key].push(string);
  });

  // 배열로 생성해 반환한다.
  return Object.values(frequency).reduce((acc, curr) => {
    acc.push(curr);
    return acc;
  }, []);
};