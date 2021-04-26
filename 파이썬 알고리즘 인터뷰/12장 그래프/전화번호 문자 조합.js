// 책의 풀이 (Runtime: 80ms, Memory: 38.3MB)
const letterCombinations = function(digits) {
  if (!digits) return [];
  
  const result = [];
  const dict = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
  };
  
  const dfs = function(index=0, path="") {
    if (path.length == digits.length) {
      result.push(path);
      return;
    }
    
    for (let idx = index; idx < digits.length; idx++) {
      const number = digits[idx];
      
      for (char of dict[number]) {
        dfs(idx + 1, path + char);
      }
    }
  };
  
  dfs();
  
  return result;
};