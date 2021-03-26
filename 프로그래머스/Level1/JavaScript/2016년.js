function solution(a, b) {
    const days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
    const targetDate = new Date(
        `2016/${a < 10 ? "0" + a : a}/${a < 10 ? "0" + b : b}`
    );

    return days[targetDate.getDay()];
}