function solution(str){
    let answer = true;
    let counter = 0; 
     
    for (let index = 0; index < str.length; index++) {
        str[index] === "("
            ? counter++
            : counter--;
    
        // counter가 음수가 되면 순서가 틀린 것이므로, 답을 false로 설정하고 반복문을 종료한다.
        if (counter < 0) {
            answer = false;
            break;
        }
    }

    // counter가 양수인 경우도 괄호의 짝이 맞지 않는 것이므로, false를 반환한다.
    return counter > 0 ? false : answer;
}