function solution(string) {
    let answer = true;
    
    if (string.length != 4 && string.length != 6) {
        answer = false;
    } 
    
    /**
     *  "5e32"과 같이 지수 형태인 경우, isNaN()을 사용하면 true가 나온다.
     *  하지만 문제에서 요구하는 것은 모든 자리의 수가 "숫지"인 것을 원하는 것이다.
     *  따라서, 문자열 요소 각각에 대해 isNaN()을 사용해야 한다. 
     **/
    for (let char of string) {
        if (isNaN(char)) {
            answer = false;
        }
    }
    
    return answer;
}