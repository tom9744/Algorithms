function solution(s, n) {
    const answer = [];
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === " ") {
            answer.push(" ");
            continue;
        }
        else {
            const ascii = s.charCodeAt(i);
            let caesar;
            
            if (ascii > 64 && ascii < 91) {
                caesar = ascii + n > 90 ? ascii + n - 26 : ascii + n;
            }
            else {
                caesar = ascii + n > 122 ? ascii + n - 26 : ascii + n;
            }
            
            answer.push(String.fromCharCode(caesar));
        }
    }
    
    return answer.join("");
}