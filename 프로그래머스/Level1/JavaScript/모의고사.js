function solution(answers) {
    const patternA = [1, 2, 3, 4, 5];  // 5
    const patternB = [2, 1, 2, 3, 2, 4, 2, 5];  // 8
    const patternC = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];  // 10
    const correct = { A: 0, B: 0, C: 0 };
    
    answers.forEach((answer, index) => {
        if (answer === patternA[index % 5]) {
            correct["A"]++; 
        }
        if (answer === patternB[index % 8]) {
            correct["B"]++; 
        }
        if (answer === patternC[index % 10]) {
            correct["C"]++; 
        }
    })
    
    const maxCorrect = Math.max.apply(null, Object.values(correct));
    
    return Object.keys(correct).reduce((acc, key, index) => {
        if (correct[key] === maxCorrect) {
            acc.push(index + 1);
        }
        return acc;
    }, []);
}