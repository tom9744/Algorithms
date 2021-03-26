function solution(arr, divisor) {
    
    const divided = arr
        .filter(elem => {
            return elem % divisor === 0;
        })
        .sort((numA, numB) => {
            return numA - numB;
        })

    return divided.length === 0 ? [-1] : divided;
}