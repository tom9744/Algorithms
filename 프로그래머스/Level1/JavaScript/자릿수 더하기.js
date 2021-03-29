function solution(n)
{
    // 숫자를 문자 배열(["1", "3", "2"...])로 변환하고, reduce로 각 자리수 합을 구한다. 
    return Array.from(String(n)).reduce((acc, curr) => {
        return acc + Number(curr);    
    }, 0);
}