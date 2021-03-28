function solution(numbers) {
    const sumSet = new Set(); // ES6에서 추가된 Set을 사용해, 중복을 제거한다.
    
    for (let i = 0; i < numbers.length - 1; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            sumSet.add(numbers[i] + numbers[j]);
        }
    }

    // Set은 Array가 아니므로, Array.from 메서드로 Array 타입으로 변환해준다.
    return Array.from(sumSet).sort((numA, numB) => numA - numB);
}