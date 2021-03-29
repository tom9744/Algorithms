function solution(n) {
    return Array.from(String(n)).map(each => Number(each)).reverse();
}