// 두 수의 범위가 -10,000,000 ~ 10,000,000이므로 O(n) 안에 풀 수 있다.
function solution(a, b) {
    let answer = 0;
    
    if (a > b) {
        let temp = a
        a = b
        b = temp
    }
    
    for (let num = a; num < b + 1; num++) {
        answer += num;
    }
    
    return a === b ? a : answer;
}