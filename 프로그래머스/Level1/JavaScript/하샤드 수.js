function solution(inpNum) {
    const digitSum = String(inpNum)
        .split("")
        .reduce((acc,curr) => acc + Number(curr), 0);
    
    return inpNum % digitSum === 0 ? true : false;
}