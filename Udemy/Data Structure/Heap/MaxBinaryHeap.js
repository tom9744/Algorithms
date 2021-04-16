/**
 * Insertion: O(logN)
 * Removal: O(logN)
 * Searching: O(N)
 * 
 * Heap은 탐색에 있어 비효율적이며, 탐색 효율성이 필요한 경우 BST를 사용한다.
 */
class MaxBinaryHeap {
    constructor() {
        this.values = [];
    }

    swap(indexA, indexB) {
        const temp = this.values[indexA];
        this.values[indexA] = this.values[indexB];
        this.values[indexB] = temp;
    }

    // O(logN)
    insert(value) {
        // 1. Add to the end
        this.values.push(value);        
        
        // 2. Bubble Up 
        let currIndex = this.values.length - 1;
        let parentIndex = Math.floor((currIndex - 1) / 2);

        // 힙의 최상단에 도착할 때까지 반복하며, 부모 노드와 값을 비교한다.
        while (currIndex > 0) {
            if (this.values[currIndex] < this.values[parentIndex]) break;
            
            this.swap(currIndex, parentIndex);
            currIndex = parentIndex;
            parentIndex = Math.floor((currIndex - 1) / 2);
        }
    }

    // O(logN)
    extractMax() {
        if (this.values.length === 0) return;

        // 1. 가장 최근에 추가된 노드와 루트 노드(= 제거 대상)의 위치를 바꾼다.
        this.swap(0, this.values.length - 1);
        
        // 2. 기존 루트 노드를 힙에서 제거한다.
        const toBeRemoved = this.values.pop();

        // 3. 힙 구조를 다듬는다. (= Sink Down)
        let currentIdx = 0;

        while (true) {
            const current = this.values[currentIdx];
            
            const leftChildIdx = (currentIdx * 2) + 1;  // 왼쪽 자식 노드의 인덱스
            const rightChildIdx = (currentIdx * 2) + 2; // 오른쪽 자식 노드의 인덱스

            // 인덱스가 힙의 최대 범위를 벗어나지 않는지 확인한 뒤, 값을 가져온다.
            const leftChild = leftChildIdx < this.values.length ? this.values[leftChildIdx] : null;
            const rightChild = rightChildIdx < this.values.length ? this.values[rightChildIdx] : null;

            let targetIdx = null;

            // 왼쪽, 오른쪽 자식 노두가 모두 존재하는 경우
            if (rightChild) {
                // 현재 노드의 위치가 올바른 경우, 반복문을 종료한다.
                if (current > leftChild && current > rightChild) break;
                // 두 자식 노드의 값이 현재 노드의 값보다 큰 경우, 둘 중 더 큰 값을 선택한다.
                if (current < leftChild && current < rightChild) targetIdx = leftChild > rightChild ? leftChildIdx : rightChildIdx;
                else if (current < leftChild) targetIdx = leftChildIdx;             
                else if (current < rightChild) targetIdx = rightChildIdx;
            } 
            // 왼쪽 자식 노드만 존재하는 경우
            else if (leftChild) {
                // 현재 노드의 위치가 올바른 경우, 반복문을 종료한다.
                if (current > leftChild) break;
                else targetIdx = leftChildIdx;
            } 
            // 어떠한 자식 노드도 존재하지 않는 경우
            else {
                break;
            }

            this.swap(currentIdx, targetIdx);
            currentIdx = targetIdx;
        }

        return toBeRemoved;
    }
}

const heap = new MaxBinaryHeap();
heap.insert(41);
heap.insert(39);
heap.insert(33);
heap.insert(18);
heap.insert(27);
heap.insert(12);
heap.insert(55);

// Index:  0   1   2   3   4   5   6
// Heap: [55, 39, 41, 18, 27, 12, 33]

heap.extractMax();  // 55

// Index:  0   1   2   3   4   5
// Heap: [33, 39, 41, 18, 27, 12]

// Index:  0   1   2   3   4   5
// Heap: [41, 39, 33, 18, 27, 12]
