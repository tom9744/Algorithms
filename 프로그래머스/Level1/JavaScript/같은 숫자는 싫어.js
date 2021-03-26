function solution(arr)
{
    const answer = [];
    
    answer.push(arr[0]);
    
    for (let i = 1; i < arr.length; i++) {
         // 정답 배열의 마지막 요소에 접근
        const lastElem = answer.slice(-1)[0]; 
        
        // 정답 배열의 마지막 요소와 현재 요소가 다른 경우에만 요소 추가
        if (lastElem != arr[i]) {
            answer.push(arr[i]);
        }
    }
    
    return answer;
}