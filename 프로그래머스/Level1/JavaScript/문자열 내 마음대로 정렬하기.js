function solution(strings, n) {
    var answer = [];
    
    strings.sort();
    strings.sort((charA, charB) => {
        return charA.charCodeAt(n) - charB.charCodeAt(n)
    })
    
    return strings;
}