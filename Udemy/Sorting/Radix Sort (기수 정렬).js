// 인자로 전달받은 자리수에 해당하는 숫자를 반환하며, 존재하지 않으면 0을 반환한다.
function getDigit(number, place) {
    const digits = String(number).split("").reverse();
    
    return place > digits.length - 1 ? 0 : +digits[place];
}

// 숫자의 자리수를 반환한다.
function digitCount(number) {
    if (number === 0) return 1;  // log10(0) => -Infinity
    return Math.floor(Math.log10(Math.abs(number))) + 1;
}

// 숫자 중 가장 자리수가 큰 숫자의 자리수를 반환한다.
function mostDigit(numbers) {
    let maxCount = -Infinity;
    numbers.forEach(number => {
        maxCount = Math.max(maxCount, digitCount(number));
    });
    return maxCount;
}

/**
 * [Best/Avg/Worst] O(N * K), N: 숫자의 개수, K: 최대 자리수
 * 
 * 기수 정렬은 Quick, Merge와 같은 비교 기반 정렬보다 빠르지만,
 * K의 값이 너무 커지게 되면, 시간 복잡도가 O(N^2)과 같아지게 된다.
 */
function radixSort(numbers) {
    const maxDigit = mostDigit(numbers);

    for (let k = 0; k < maxDigit; k++) {
        // 진법에 따라 Bucket을 생성한다.
        const buckets = Array.from({length: 10}, () => []);

        numbers.forEach(number => {
            const kthDigit = getDigit(number, k); // K번째 자리의 수를 구한다.

            buckets[kthDigit].push(number); // 숫자에 해당하는 Bucket에 추가한다.
        });
    
        numbers = [].concat(...buckets); // Bucket에서 다시 꺼내 배열에 합친다.
    }

    return numbers;
}

radixSort([321, 432, 534, 567, 343, 483, 293, 3494, 300]);