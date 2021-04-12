function swap(array, indexA, indexB) {
    const temp = array[indexA];
    array[indexA] = array[indexB];
    array[indexB] = temp;
}

// Best/Avg/Worst: O(N^2)
function bubbleSort(array) {
    for (let i = array.length - 1; i > 0; i--) {
        for (let j = 0; j < i; j++) {
            // 앞의 원소가 뒤의 원소보다 크면 자리를 바꾼다.
            if (array[j] > array[j + 1]) {
                swap(array, j, j + 1);
            } 
        }
    }

    return array;
}

// Best: O(N), Avg/Worst: O(N^2)
function optimizedBubbleSort(array) {
    for (let i = array.length - 1; i > 0; i--) {
        let isSorted = true;

        for (let j = 0; j < i; j++) {
            // 앞의 원소가 뒤의 원소보다 크면 자리를 바꾼다.
            if (array[j] > array[j + 1]) {
                swap(array, j, j + 1);
                isSorted = false;
            } 
        }

        // [최적화] 단 한번도 Swap이 발생하지 않은 경우, 종료한다.
        if (isSorted) break;
    }

    return array;
}