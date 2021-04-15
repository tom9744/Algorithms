function solution(requests, budget) {
    const sortedRequest = requests.sort((numA, numB) => numB - numA);
    let answer = 0;
    
    while(true) {
        const request = sortedRequest.pop();
        
        if (budget - request >= 0) {
            budget -= request;
            answer++;
        } else {
            break;
        }
    }

    return answer;
}