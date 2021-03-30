function solution(num) {
    let answer = 0;
    
    while (num !== 1) {
        // 500번 이상 반복한 경우, answer를 -1로 바꾸고 중단.
        if (answer > 500) {
            answer = -1;
            break;
        }

        // switch-case문을 이용해 짝수, 홀수에 적절한 연산 처리.
        switch(num % 2 === 0) {
            case true:
                num /= 2;
                break;
            case false:
                num = (num * 3) + 1;
                break;
            default:
                break;
        }
        
        answer++;
    }
    
    return answer;
}