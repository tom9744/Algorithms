class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

/**
 * Insertion: O(1)
 * Removal: O(1)
 * Searching: O(N)
 * Access: O(N)
 * 
 * 큐는 데이터의 추가/삭제에 특화된 자료구조로, 시간 복잡도가 모두 O(1)이다.
 */
class Queue {
    constructor() {
        this.front = null;
        this.back = null;
        this.size = 0;
    }

    // enqueue()는 O(1)이기 때문에, 단방향 연결 리스트의 push() 메서드를 이용한다.
    enqueue(newVal) {
        const newNode = new Node(newVal);

        if (this.front === null) {
            this.front = newNode;
            this.back = newNode;
        } else {
            const lastNode = this.back;
            lastNode.next = newNode;
            this.back = newNode;
        }

        this.size++;

        return this;
    }

    // dequeue()는 O(1)이기 때문에, 단방향 연결 리스트의 shift() 메서드를 이용한다.
    dequeue() {
        if (this.front === null) return;

        // 큐의 맨 앞에 위치한 노드를 변수에 저장한다.
        const targetNode = this.front; 
        
        // 마지막 요소를 제거하는 경우라면, back을 null로 설정한다.
        if (this.front === this.back) {
            this.back = null;
        }

        // 제거할 노드의 다음 노드를 새로운 Front로 설정한다.
        this.front = targetNode.next;
     
        this.size--;

        return targetNode.value;
    }
}

const queue = new Queue();