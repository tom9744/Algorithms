function swap(array, indexA, indexB) {
    const temp = array[indexA];
    array[indexA] = array[indexB];
    array[indexB] = temp;
}

// Best/Avg/Worst: O(N^2)
function selectionSort(array) {
    // 1. 배열의 맨 앞부터 요소를 선택한다.
    for (let i = 0; i < array.length; i++) {
        let minValIndex = i;

        // 2. 선택된 요소 이후에 존재하는 요소 중 최소값을 찾는다.
        for (let j = i + 1; j < array.length; j++) {
            if (array[i] < array[minValIndex]) {
                minValIndex = j;
            }
        }

        if (minValIndex !== i) {
            // 3. 선택한 요소와 최소값 요소를 바꾼다.
            swap(array, i, minValIndex);
        }
    }
    return array;
}

