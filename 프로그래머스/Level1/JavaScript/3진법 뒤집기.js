function solution(n) {
    const ternary = [];
    
    // 3진법으로 변환한다.
    while (n != 0) {
        ternary.push(n % 3);
       
        n = Math.floor(n / 3);
    }

    // 3진법을 10진법으로 변환한 뒤, reduce() 메서드를 통해 합계를 구한다.
    return ternary.map((ternaryNumer, index) => {
            return ternaryNumer * (3 ** (ternary.length - 1 - index));        
        })
        .reduce((accumulator, current) => {
            return accumulator + current
        }, 0);
}