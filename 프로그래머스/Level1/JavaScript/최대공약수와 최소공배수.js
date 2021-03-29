function solution(n, m) {
    if (n < m) {
        const temp = n;
        n = m;
        m = temp;
    }
    
    const multiplied = Math.abs(n * m);
    
    // 유클리드 호제법 gcd(a, b) = gcd(b, r) (where, r = a % b)
    while (m !== 0) {
        const remainder = n % m;
        n = m;
        m = remainder;
    }
    
    return [n, multiplied / n];
}