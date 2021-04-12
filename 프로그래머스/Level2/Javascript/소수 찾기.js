function getPermutation(numbers, count) {
    const result = [];
    // [Base Case] 순열의 길이가 1인 경우, 요소 각각을 배열로 만들어 반환
    if (count === 1) return numbers.map(num => [num]);
    
    numbers.forEach((num, i, arr) => {
        const fixer = num; // 고정할 숫자
        const rest = arr.filter((_, j) => i !== j); // 고정한 숫자를 제외한 나머지 배열
        const permutations = getPermutation(rest, count - 1); // 부분 순열 구하기
        const attached = permutations.map(permutation => [fixer, ...permutation]); // 부분 순열에 고정한 숫자 연결
        result.push(...attached); // 결과에 추가
    })

    return result;
}

function isPrime(number) {
    if (number <= 1) return false; // 1보다 작으면 소수 X
    if (number % 2 === 0) return false; // 2로 나누어 떨어지면 소수 X
    if (number === 2 || number === 3) return true; // 2와 3은 소수 O 

    // 최초 3부터 시작해, 숫자의 제곱근 사이의 홀수로 나누어 보면서 소수 판별 수행 
    for (let divisor = 3; divisor <= Math.sqrt(number); divisor += 2) {
        // 나누어 떨어지는 수가 있는 경우 소수 X
        if (number % divisor === 0) return false; 
    }
    
    return true;
}

function solution(numbers) {
    const numberSet = new Set(); // Set을 사용한 중복 제거 - O(1)
    
    for (let num = 1; num <= numbers.length; num++) {
        getPermutation(numbers.split(""), num).forEach(perm => {
            numberSet.add(+perm.join(""));
        });
    }

    // 만든 숫자 중, 소수인 것의 개수를 반환
    return Array.from(numberSet).filter(number => isPrime(number)).length;
}