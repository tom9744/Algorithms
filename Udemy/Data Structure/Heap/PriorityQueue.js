class Node {
    // Priority 값이 작은 것이 높은 우선순위를 가진다.
    constructor(value, priority) {
        this.value = value;
        this.priority = priority;
    } 
}

class PriorityQueue {
    constructor() {
        this.values = [];
    }

    _swap(idxA, idxB) {
        const temp = this.values[idxA];
        this.values[idxA] = this.values[idxB];
        this.values[idxB] = temp;
    }

    enqueue(newVal, priority) {
        const newNode = new Node(newVal, priority);

        // 1. 힙을 표현한 배열의 마지막에 추가한다.
        this.values.push(newNode);

        // 2. 힙을 재정렬 한다. (= Bubble Up) 
        let currIdx = this.values.length - 1;
        let parentIdx;

        while (currIdx > 0) {
            parentIdx = Math.floor((currIdx - 1) / 2);

            const currPriority = this.values[currIdx].priority;
            const parentPriority = this.values[parentIdx].priority;

            // 자식 노드와 부모 노드가 최소힙의 정의를 따르는 경우, 반복문을 종료한다.
            if (currPriority > parentPriority) break;

            // 그렇지 않은 경우, 부모 노드와 지식 노드의 위치를 바꾼다.
            this._swap(currIdx, parentIdx);
            currIdx = parentIdx;
        }

        return this;
    }

    dequeue() {
        if (this.values.length === 0) return;

        // 1. 힙의 루트 노드와 가장 최근에 추가된 노드의 자리를 바꾼다.
        this._swap(0, this.values.length - 1);

        // 2. 힙의 크기를 줄인다. (= 마지막 요소를 제거한다.)
        const toBeRemoved = this.values.pop();

        // 3. 힙을 재정렬 한다. (= Sink Down)
        let currIdx = 0;
        let leftChildIdx, rightChildIdx;

        while (currIdx < this.values.length) {
            leftChildIdx = (2 * currIdx) + 1;
            rightChildIdx = (2 * currIdx) + 2;

            // 3-1. 루트 노드와 두 자식을 비교해, 더 작은 값이 있으면 위치를 바꾼다.
            const current = this.values[currIdx].priority;
            const left = leftChildIdx < this.values.length 
                ? this.values[leftChildIdx].priority 
                : null;
            const right =  rightChildIdx < this.values.length 
                ? this.values[rightChildIdx].priority
                : null;
            
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

const pqueue = new PriorityQueue();
pqueue.enqueue(10, 3);
pqueue.enqueue(10, 4);
pqueue.enqueue(10, 5);
pqueue.enqueue(10, 1);