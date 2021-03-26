function solution(array, commands) {
    const answer = [];
    
    for (const command of commands) {
        const [startIdx, endIdx, targetIdx] = command;  // 배열 구조 분해 할당
        const slicedAndSorted = array.slice(startIdx - 1, endIdx).sort((numA, numB) => numA - numB);
        answer.push(slicedAndSorted[targetIdx - 1]);    
    }

    return answer;
}