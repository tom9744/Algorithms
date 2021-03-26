function solution(s){
    let pCount = 0;
    let yCount = 0;
    
    for (const char of s.toLowerCase()) {
        if (char === "p") pCount++;
        else if (char === "y") yCount++;
    }
    
    // 중첩 삼항 연산자를 이용해 결과를 출력한다.
    return pCount === yCount ? (pCount === 0 ? false : true) : false;
}