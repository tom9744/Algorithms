// 나의 풀이 (Runtime: 104ms, Memory: 42MB)
const permute = function(nums) {
  temp = [];
  result = [];
  
  const get_permutation = function(elements) {
    if (elements.length === 0) {
      result.push(temp.slice());  // 참조가 아닌 복사본을 추가한다.
      return;
    }
    
    for (let elem of elements) {
      const rest = elements.filter(el => el !== elem);
      
      temp.push(elem);
      get_permutation(rest);
      temp.pop();  // 백트래킹
    }
  }
  
  get_permutation(nums);
  
  return result;
};