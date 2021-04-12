// Best: O(N), Avg/Worst: O(N^2)
function insertionSort(array) {
    for (let i = 1; i < array.length; i++) {
        let currentVal = array[i];
        
        // 현재 요소의 앞쪽의 이미 정렬된 부분과 비교하며, 삽입할 자리를 찾는다.
        for (var j = i - 1; j >= 0; j--) {
            if (array[j] < currentVal) {
                break;
            } else {
                // 현재 요소가 더 작은 경우, 기존 요소들을 오른쪽으로 한 칸씩 이동시킨다.
                array[j + 1] = array[j];
            }
        }
        array[j + 1] = currentVal;
    }
    return array;
}