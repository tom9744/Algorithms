function solution(s) {
    // reverse()는 배열 원소를 뒤집을 뿐, 정렬하지는 않는다.
    return s.split("").sort().reverse().join("");
}