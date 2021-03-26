function solution(n, lost, reserve) {
    // 체육복의 여벌 소유 여부, 분실 여부를 반영해 학생 별로 가지고 있는 체육복의 수를 정의한다.
    const trainingWares = new Array(n).fill(1).map((each, index) => {
        if (lost.includes(index + 1)) each--;
        if (reserve.includes(index + 1)) each++;
        return each;
    });
    
    // 체육복이 없는 학생의 앞, 뒤 학생 중 한명이라도 여벌을 가지고 있다면 빌려준다.
    for (let idx = 0; idx < trainingWares.length; idx++) {
        if (trainingWares[idx] === 0) {
            if (trainingWares[idx - 1] == 2) {
                trainingWares[idx]++;
                trainingWares[idx - 1]--;   
            }
            else if (trainingWares[idx + 1] == 2) {
                trainingWares[idx]++;
                trainingWares[idx + 1]--;   
            }
        }
    }
    
    // reduce() 메서드를 이용해 체육복을 1개 이상 소지한 학생의 수를 센다.
    return trainingWares.reduce((acc, curr) => curr > 0 ? acc + 1 : acc, 0);
}