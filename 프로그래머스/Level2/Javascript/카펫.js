function solution(brown, yellow) {
    
    const fourSideLength = brown + 4; // 카펫의 전체 외곽 변 길이의 합  
    const twoSideLength = Math.floor(fourSideLength / 2); // 세로 변, 가로 변 길이의 합
    
    // 가로 길이가 세로 길이보다 같거나 크다고 하였으므로, 절반만 탐색한다.
    for (let row = 1; row < Math.ceil(twoSideLength / 2) + 1; row++) {
        const col = twoSideLength - row;
        const yellowArea = (row - 2) * (col -2); // 노란색 영역의 넓이
        
        if (yellowArea === yellow) {
            return [col, row];
        }
    }
}