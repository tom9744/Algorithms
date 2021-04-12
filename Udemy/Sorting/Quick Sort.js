function swap(array, indexA, indexB) {
    const temp = array[indexA];
    array[indexA] = array[indexB];
    array[indexB] = temp;
}

/**
 * 배열의 가장 첫번째 요소를 Pivot으로 설정한다. 
 * Pivot보다 값이 작은 요소를 발견하면, 왼쪽으로 이동시키고 개수를 센다 (= swapIndex)
 * 마지막으로 Pivot을 알맞은 위치 (= swapIndex)로 이동시킨다. 
 */
function pivot(array, start = 0, end = array.length - 1) {
    const pivot = array[start];
    let swapIndex = start;

    for (let index = start + 1; index < array.length; index++) {
        if (pivot > array[index]) {
            swapIndex++;
            swap(array, swapIndex, index);
        }
    }
    swap(array, start, swapIndex);

    return swapIndex;
}
/**
 * [Best/Avg] O(NlogN) / Decomposition - O(logN), Merging - O(N)
 * [Worst] O(N^2) / Decomposition - O(N), Merging - O(N)
 * 
 * 배열이 이미 정렬되어 있는 경우, 맨 앞 요소를 Pivot으로 설정하면 Worst Case이다.
 * 따라서, 무작위로 Pivot을 선택하도록 하는 방법이 있다.
 */
function quickSort(array, left = 0, right = array.length - 1) {
    // 재귀호출이 반복됨에 따라 left와 right의 거리가 가까워지며
    // left와 right가 같아지면 재귀호출이 종료되어야 한다.
    if (left < right) {
        const pivotIndex = pivot(array, left, right);
        quickSort(array, left, pivotIndex - 1);
        quickSort(array, pivotIndex + 1, right);
    }
    return array;
}

// 