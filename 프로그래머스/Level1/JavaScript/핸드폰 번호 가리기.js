function solution(phoneNumber) {
    const length = phoneNumber.length;
    
    return phoneNumber
        .split("")
        .map((num, index) => index < length - 4 ? "*" : num)
        .join("");
}