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
 * 스택은 데이터의 추가/삭제에 특화된 자료구조로, 시간 복잡도가 모두 O(1)이다.
 */
class Stack {
    constructor() {
        this.top = null;
        this.bottom = null;
        this.size = 0;
    }

    // Stack의 push()는 O(1)이기 때문에, 단방향 연결 리스트의 unshift() 메서드를 이용한다.
    push(newVal) {
        const newNode = new Node(newVal);

        if (this.top === null) {
            this.top = newNode;
            this.bottom = newNode;
        } else {
            newNode.next = this.top;
            this.top = newNode;
        }

        this.size++;

        return this;
    }

    // Stack의 pop()는 O(1)이기 때문에, 단방향 연결 리스트의 shift() 메서드를 이용한다.
    pop () {
        if (this.top === null) return;

        const poppedNode = this.top; // 스택의 위에서 첫번째 노드를 변수에 저장한다.

        this.top = poppedNode.next; // 두번째 노드를 새로운 Top으로 설정한다.

        poppedNode.next = null; // 제거될 노드의 next 속성을 초기화한다.
        
        if (this.size === 1) {
            this.bottom = null;
        }
        this.size--;

        return poppedNode.value;
    }
}

const stack = new Stack();