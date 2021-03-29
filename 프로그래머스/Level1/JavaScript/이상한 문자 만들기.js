function solution(s) {
    
    // 공백 문자(" ")를 기준으로 단어를 자르고, map()을 호출한다.
    const parts = s.split(" ").map(part => {
        // 각 단어를 문자 단위로 자르고, 인덱스에 따라 대/소문자로 변환한다. 
        return part.split("").map((elem, index) => {
            if (index % 2 === 0) {
                return elem.toUpperCase();    
            }
            else {
                return elem.toLowerCase();
            }
        }).join("");  // 문자들을 다시 하나의 단어로 합치고 반환한다.
    }).join(" "); // 단어들을 하나의 문장으로 합치고 반환한다.
    
    return parts;
}