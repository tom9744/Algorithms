function solution(s) {
    const middleIdx = Math.floor(s.length / 2);
    
    // 삼항 연산자를 이용해, 짝수인 경우와 홀수인 경우 자르는 범위를 다르게 설정한다.
    return s.length % 2 === 0 ? 
        s.slice(middleIdx - 1, middleIdx + 1) : 
        s.slice(middleIdx, middleIdx + 1);
}