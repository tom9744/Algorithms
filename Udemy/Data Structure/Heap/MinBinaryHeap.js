class MinBinaryHeap {
    constructor() {
        this.values = [];
    }

    _swap(indexA, indexB) {
        const temp = this.values[indexA];
        this.values[indexA] = this.values[indexB];
        this.values[indexB] = temp;
    }

    insert(newVal) {
        // 1. 힙을 표현한 배열의 맨 마지막에 추가한다.
        this.values.push(newVal);

        let currIdx = this.values.length - 1;
        let parentIdx;

        // 2. 힙을 재정렬한다.
        while (currIdx > 0) {
            parentIdx = Math.floor((currIdx - 1) / 2);

            const parent = this.values[parentIdx];
            const current = this.values[currIdx];

            if (current > parent) break;

            // 자식 노드보다 부모 노드의 값이 크면, 위치를 바꾼다.
            this._swap(currIdx, parentIdx);
            currIdx = parentIdx;
        }

        return this.values;
    }

    extractMin() {
        if (this.values.length === 0) return;
        
        // 1. 힙의 루트 노드와 가장 최근에 추가된 노드의 자리를 바꾼다.
        this._swap(0, this.values.length - 1);

        // 2. 힙의 크기를 줄인다. (= 마지막 요소를 제거한다.)
        const toBeRemoved = this.values.pop();

        // 3. 힙을 재정렬 한다. (= Sink Down)
        let currIdx = 0;
        let leftChildIdx, rightChildIdx;

        while (true) {
            leftChildIdx = (2 * currIdx) + 1;
            rightChildIdx = (2 * currIdx) + 2;

            // 3-1. 루트 노드와 두 자식을 비교해, 더 작은 값이 있으면 위치를 바꾼다.
            const current = this.values[currIdx];
            const left = leftChildIdx < this.values.length ? this.values[leftChildIdx] : null;
            const right =  rightChildIdx < this.values.length ? this.values[rightChildIdx] : null;
            
            let targetIdx;

            if (right) {
                // 3-2. 두 자식의 값이 모두 작으면, 더 작은 값을 가진 자식과 위치를 바꾼다.
                if (left < current && right < current) targetIdx = left < right ? leftChildIdx : rightChildIdx; 
                else if (left < current) targetIdx = leftChildIdx;
                else if (right < current) targetIdx = rightChildIdx;
            } 
            else if (left) {
                if (left < current) targetIdx = leftChildIdx;
            }

            // 3-3. 두 자식이 모두 부모 노드보다 큰 값을 가지면, 반복문을 종료한다. 
            if (!targetIdx) break;

            this._swap(currIdx, targetIdx);
            currIdx = targetIdx;
        }

        return toBeRemoved;
    }
}

const heap = new MinBinaryHeap();