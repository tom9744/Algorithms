function solution(arr) {
    // Math.min(..arr)도 가능하다!
    const minVal = Math.min.apply(null, arr);
    const minIdx = arr.findIndex(elem => elem === minVal);
    
    // arr.splice(startIdx, deleteCount, [newElems...])
    arr.splice(minIdx, 1);
    
    return arr.length !== 0 ? arr : [-1];
}