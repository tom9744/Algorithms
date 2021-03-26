function solution(nums) {
    const kinds = {}; 
    
    nums.forEach(num => {
        if (!kinds[num]) {
            kinds[num] = 1;
        }
        else {
            kinds[num]++;
        }
    })
    
    /**
     * 폰켓몬 종류의 수가 N/2보다 크면, 최대로 고를 수 있는 경우의 수는 N/2이다.
     * 그렇지 않은 경우, 주어진 폰켓몬 종류의 수 만큼 뽑는 것이 최선이다.
     */
    return Object.keys(kinds).length > nums.length / 2 ? nums.length / 2 : Object.keys(kinds).length;
}