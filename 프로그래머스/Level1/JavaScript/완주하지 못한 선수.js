function solution(participant, completion) {
    const part = {};
    
    // 참가자의 이름을 key로 갖는 속성을 객체에 추가한다.
    for (let each of participant) {
        // 이미 추가된 이름인 경우, 중복 처리한다.
        if (part[each]) {
            part[each]++;
        }
        else {
            part[each] = 1;   
        }
    }

    // 완주자의 이름이 객체 존재하는지 확인한다.
    for (let each of completion) {
        if (part[each] && part[each] > 0) {
            part[each]--;
            // 완주자의 이름을 key로 가지는 속성의 value가 0이면 삭제한다.
            if (part[each] === 0) {
                delete part[each];
            }
        }
    }
    
    // 객체에 마지막까지 남아 있는 속성의 key를 출력하면 정답이다.
    return Object.keys(part)[0];
}