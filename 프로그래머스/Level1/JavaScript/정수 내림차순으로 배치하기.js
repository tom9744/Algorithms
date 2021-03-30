function solution(n) {
    const answer = String(n)
        .split("")  // 문자열을 문자 단위로 잘라 배열로 만든다. 
        .map(chr => Number(chr))  // 각 문자를 숫자로 변환한다. (필요...?)
        .sort((numA, numB) => numB - numA)  // 내림차순 정렬한다.
        .join("")  // 다시 문자열로 합친다.
    
    return Number(answer);
}