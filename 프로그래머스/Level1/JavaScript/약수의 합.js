function solution(n) {
    const numbers = [];
    
    for (let num = 1; num < n + 1; num++) {
        numbers.push(num);
    }
    
    // filter로 약수만 남기고, reduce로 합을 구한다.
    return numbers.filter((number) => {
            return n % number === 0;
        })
        .reduce((acc, curr) => {
            return acc + curr;
        });
}