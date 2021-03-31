function getCombinations(arr, selectNumber) {
    const result = [];
    if (selectNumber === 1) {
        return arr.map(value => [value]);
    }
    
    arr.forEach((fixer, idx, fullArr) => {
        const rest = fullArr.slice(idx + 1);
        const combinations = getCombinations(rest, selectNumber - 1);
        const attached = combinations.map(combination => [fixer, ...combination]);
        result.push(...attached);
    });
    
    return result;
};

function isPrime(number) {
    for (let num = 2; num < (number ** 0.5) + 1; num++) {
        if (number % num === 0) {
            return false;
        }
    }
    return true;
}

function solution(nums) {
    
    const answer = getCombinations(nums, 3)
        .map(combination => combination.reduce((acc, curr) => acc + curr, 0))
        .filter(sum => isPrime(sum))
        .length;
    
    return answer;
}