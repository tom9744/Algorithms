function solution(numbers) {
    const answer = numbers
        .map(elem => elem + "")
        .sort((numA, numB) => Number(numB + numA) - Number(numA + numB))
        .join("");
    
    return answer[0] === "0" ? "0" : answer;
}