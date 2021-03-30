function solution(n) {
    const x = Math.sqrt(n);

    // 양의 정수 n의 제곱근 x가 정수라면, n은 x의 제곱인 것이다. 
    return Number.isInteger(x) ? (x + 1) ** 2 : -1;
}