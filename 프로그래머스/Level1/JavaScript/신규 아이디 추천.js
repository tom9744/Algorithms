function solution(newId) {
    
    let filteredId = newId
        // [1] 모든 대문자를 대응되는 소문자로 치환합니다.
        .toLowerCase() 
        .split("")
        // [2] 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
        .filter(each => {
            return /[a-z0-9-_.]/.test(each);
        });
    
    // [3] 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    const DP = Array(filteredId.length - 1).fill(0);
    DP[0] = filteredId[0] === "." ? 1 : 0;
    for (let idx = 1; idx < filteredId.length; idx++) {
        DP[idx] = filteredId[idx] === "." ? (filteredId[idx - 1] === "." ? DP[idx - 1] + 1 : 1) : 0; 
    }
    filteredId = filteredId.filter((each, idx) => DP[idx] <= 1); 
    
    // [4] 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if (filteredId[0] === ".") {
        filteredId.splice(0, 1);
    }
    if (filteredId[filteredId.length - 1] === ".") {
        filteredId.splice(-1, 1);
    }

    // [5] 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if (filteredId.length === 0) {
        filteredId.push("a");
    }

    // [6] 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if (filteredId.length > 15) {
        filteredId = filteredId.slice(0, 15);
        // [6-1] 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
        if (filteredId[14] === ".") {
            filteredId.splice(-1, 1);
        }
    }
    
    // [7] 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if (filteredId.length < 3) {
        while (filteredId.length < 3) {
            filteredId.push(filteredId[filteredId.length - 1]);
        } 
    }

    return filteredId.join("");
}