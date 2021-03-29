function solution(a, b) {
    
    // reduce() 메서드는 (누적값, 현재값, 인덱스, 전체배열)을 매개변수로 가진다.
    const answer = a.reduce((acc, curr, idx) => {
        return acc + (curr * b[idx]);
    }, 0)

    return answer;
}