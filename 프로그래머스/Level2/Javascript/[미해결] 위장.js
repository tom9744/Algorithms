function solution(clothes) {
    const hashTable = {};
    let counter = 1;

    clothes.forEach(([name, type]) => {
        !hashTable[type] 
            ? hashTable[type] = 1
            : hashTable[type]++;
    })
    
    // 모든 경우의 수를 구한다.
    Object.keys(hashTable).forEach(key => {
        counter *= hashTable[key] + 1;
    })
    
    // 아무것도 입지않는 경우를 제외한다.
    return counter - 1;
}