// 나의 풀이 (Runtime: 152ms, Memory: 46.7MB)
const combine = function(n, k) {
    const result = [];
    const prevNumbers = [];
    const numbers = [];
    for (let i = 1; i <= n; i++) {
        numbers.push(i);
    }
    
    const combination = function(numbers, count) {
        // 주어진 조합의 길이를 달성한 경우, 함수를 종료한다.
        if (count === 0) {
            result.push(prevNumbers.slice());
            return;
        }
        
        numbers.forEach((number, idx, fullArr) => {
            // 자신과 자신 이전의 숫자를 제외한 배열을 생성한다.
            const nextNumbers = fullArr.slice(idx + 1);
            
            prevNumbers.push(number);
            combination(nextNumbers, count - 1);
            prevNumbers.pop(); // 백트래킹
        })
    }
    
    combination(numbers, k);
    
    return result;
};