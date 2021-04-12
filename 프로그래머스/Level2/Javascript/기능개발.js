function solution(progresses, speeds) {
    var answer = [];
    
    while (progresses.length > 0) {
        // 각 작업에 대한 진척도를 반영한다.
        progresses = progresses.map((progress, index) => {
            const nextProgress = progress + speeds[index];
            return nextProgress > 100 ? 100 : nextProgress;
        })
        
        // 가장 첫번째 작업이 완료된 경우,
        if (progresses[0] === 100) {
            // 종료되지 않은 첫번째 작업의 인덱스를 구한다.
            const workInProgressIndex = progresses.findIndex(progress => progress < 100);
            
            // 종료되지 않은 작업이 없다면,
            if (workInProgressIndex === -1) {
                // 현재 Queue에 존재하는 모든 작업의 개수를 추가하고 종료한다. 
                answer.push(progresses.length);
                break;
            }

            // 종료된 작업들을 작업 진도, 작업 속도 배열에서 모두 제거한다.
            answer.push(workInProgressIndex);
            speeds = speeds.slice(workInProgressIndex);
            progresses = progresses.slice(workInProgressIndex);            
        }
    }
    
    return answer;
}