function solution(n) {
    const numbers = new Array(n + 1).fill(true);
    numbers.splice(0, 2, false, false);

    // 에라토스테네스의 체
    for (let i = 2; i < (n ** 0.5) + 1; i++) {
        if (numbers[i]) {
            for (let j = i + i; j < n + 1; j += i) {
                numbers[j] = false;
            }
        }
    }

    const primes = numbers.filter((isPrime, index) => {
        return isPrime;
    })

    return primes.length;
}