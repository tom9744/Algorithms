// Time Complexity O(2^n) - Exponential
function recursiveFibonacci(number) { 
  if (number <= 2) return 1;
  return recursiveFibonacci(number - 1) + recursiveFibonacci(number - 2);
}

console.log(recursiveFibonacci(5));   // 5
console.log(recursiveFibonacci(10));  // 55
console.log(recursiveFibonacci(100)); // It takes forever!