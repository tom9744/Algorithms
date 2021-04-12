/**
 *   1    1    1
 *   2    2    2
 *   3   10    4 
 *   4   11   11
 *   5   12   12
 *   6   20   14
 *   7   21   21
 *   8   22   22
 *   9  100   24
 *  10  101   41 
 */
function solution(num) {
    const digits = ["4", "1", "2"];
    let answer = "";
    
    // 기본적으로 10진법 → 3진법 변환을 수행한다. 
    while (num > 0) {
        const remainder = num % 3;
        answer = digits[remainder] + answer;

        // 정수를 3으로 나눈 나머지가 0이면, 몫에 -1을 해준다.
        num = (remainder === 0) 
            ? Math.floor(num / 3) - 1
            : Math.floor(num / 3);
    }
    
    return answer;
}