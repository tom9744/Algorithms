function solution(priorities, location) {
    let answer = 0;
    
    while (true) {
        const maxPriority = Math.max.apply(null, priorities);
        const current = priorities.shift();

        // 맨 앞 문서의 우선순위가 최대값과 같은 경우, 인쇄 처리한다.
        if (current === maxPriority) {
            answer++;
            // 방금 인쇄한 문서가 내가 요청한 것이었다면, 반복문을 중단한다.
            if (location === 0) {
                break;
            }
        } 
        // 맨 앞 문서의 우선순위가 최대값보다 작은 경우, Queue의 맨 뒤로 보낸다.
        else {
            priorities.push(current);
        }

        // 문서 위치를 갱신한다.
        location = location === 0 ? priorities.length - 1 : location - 1;
    }
    
    return answer;
}