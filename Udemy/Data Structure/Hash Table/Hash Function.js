/**
 * 다음 세 개의 이유로, 좋은 해시 함수라고 할 수 없다.
 * 
 * 1. 문자열 자료형의 Key만 처리할 수 있다.
 * 2. 반복문을 사용해 시간 복잡도가 O(N)이다.
 * 3. 결과값이 쉽게 편향될 수 있다.
 */
function badHash(key, arrayLength) {
    let total = 0;
    for (let char of key) {
        // 문자열의 ASCII 코드를 사용해 Index로 변환한다.
        const value = char.charCodeAt(0) - 96;
        total = (total + value) % arrayLength;
    }
    return total;
}

/**
 * 위의 해시 함수를 개선한 것이다.
 */
 function impovedHash(key, arrayLength) {
    // 소수를 사용하면, 결과값이 편향되는 것을 방지할 수 있다.
    const WEIRD_PRIME = 31;
    let total = 0;
    
    // 문자열의 길이가 100보다 큰 경우, 100번만 반복문을 수행한다.
    for (let i = 0; i < Math.min(key.length, 100); i++) {
        const char = key[i];
        const value = char.charCodeAt(0) - 96;
        total = (total * WEIRD_PRIME + value) % arrayLength;
    }
    return total;
}

badHash("pink", 10);        // 0
badHash("orangered", 10);   // 7
badHash("cyan", 10);        // 3

