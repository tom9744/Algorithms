function solution(n) {
    const tempStorage = [];
    
    // 삼항 연산자를 사용해 코드의 길이를 단축한다.
    for (let i = 0; i < n; i++) {
        tempStorage.push(i % 2 === 0 ? "수" : "박");
    }
    
    // 배열을 문자열로 합친 것을 출력한다.
    return tempStorage.join("");
}