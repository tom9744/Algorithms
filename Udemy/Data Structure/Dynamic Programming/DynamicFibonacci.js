// 나의 풀이 (Bottom-Up)
function memoizationFibonacci(number) {
  const memo = [0, 1, 1];

  for (let num = 3; num <= number; num++) {
    memo[num] = memo[num - 1] + memo[num - 2];
  }

  return memo.pop();
}

console.log(memoizationFibonacci(5));   // 5
console.log(memoizationFibonacci(10));  // 55
console.log(memoizationFibonacci(100)); // 354224848179262000000

// 강좌에서 제시한 풀이 (Top-Down)
function answerFibonacci(number, memo = []) {
  if (memo[number]) return memo[number];
  if (number <= 2) return 1;

  const result = answerFibonacci(number - 1, memo) + answerFibonacci(number - 2, memo);
  memo[number] = result;

  return result;
}

console.log(answerFibonacci(5));    // 5
console.log(answerFibonacci(10));   // 55
console.log(answerFibonacci(100));  // 354224848179262000000