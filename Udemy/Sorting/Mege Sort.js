// Time Complexity is O(m + n), where m and n are the lengths of arrays.
function merge(sortedArrayA, sortedArrayB) {
    const mergedArray = [];
    
    while (true) {
        // 배열 A의 요소가 먼저 고갈되면, 배열 B의 남은 요소들을 연결한다.
        if (sortedArrayA.length === 0) {
            mergedArray.push(...sortedArrayB);
            break;
        }

        // 배열 B의 요소가 먼저 고갈되면, 배열 A의 남은 요소들을 연결한다.
        if (sortedArrayB.length === 0) {
            mergedArray.push(...sortedArrayA);
            break;
        }

        // 정렬된 두 배열의 가장 앞 요소를 비교해 더 작은 수를 선택한다.
        const smallest = sortedArrayA[0] < sortedArrayB[0] 
            ? sortedArrayA.splice(0, 1)
            : sortedArrayB.splice(0, 1);   

        mergedArray.push(smallest[0]);  
    }

    return mergedArray;
}

// Best/Avg/Worst: O(NlogN)
function mergeSort(array) {
    // 배열 길이가 0 또는 1이면, 배열 자체를 반환해 재귀호출을 끝낸다.
    if (array.length <= 1) {
        return array;
    }    

    const middle = Math.floor(array.length / 2);
    // 왼쪽, 오른쪽 절반에 대해 mergeSort를 재귀호출한다.
    const left = mergeSort(array.slice(0, middle)); 
    const right = mergeSort(array.slice(middle));

    // merge를 호출해 부분 배열을 정렬하며 합병한다.
    return merge(left, right);
}

mergeSort([1, 3, 5, 2, 4, 9, 10]);

// [1, 3, 5]    
// [1]
//    [3, 5]    
//    [3][5]    
// [1][3, 5]    
// [1, 3, 5]    

// [2, 4, 9, 10]
// [2][4]
// [2, 4]
//       [9][10]
//       [9, 10]
// [2, 4][9, 10]   
// [2, 4, 9, 10]

// [1, 3, 5][2, 4, 9, 10]
// [1, 2, 3, 4, 5, 9, 10]