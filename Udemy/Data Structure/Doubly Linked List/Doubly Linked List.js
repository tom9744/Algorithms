class Node {
    constructor(value) {
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}

/**
 * Insertion: O(1)
 * Removal: O(1)
 * Searching: O(N)
 * Access: O(N)
 * 
 * 데이터에 대한 접근/수정보다 추가/삭제가 많을 경우, 배열(Array)에 비해 유리하다.
 */
class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    // O(1)    
    push(newVal) {
        const newNode = new Node(newVal);
        
        // 리스트가 비어있는 경우, 새로 생성한 노드를 Head와 Tail로 설정한다. 
        if (this.head === null) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode; // 새로 생성한 노드를 기존 Tail의 next에 연결한다.
            newNode.prev = this.tail; // 새로 생성한 노드의 prev에 기존 Tail을 연결한다.
            this.tail = newNode;      // 리스트의 Tail을 새로 생성한 노드로 변경한다.
        }

        // 리스트의 길이를 증가시킨다.
        this.length++;

        return this;
    }

    // O(1) - 단방향 연결 리스트의 pop()은 O(N) 시간 복잡도를 가진다.
    pop() {
        // 리스트에 아무런 요소가 없으면, undefined를 반환한다.
        if (this.head === null) return;

        // 리스트의 Tail(= 제거할 요소)를 변수에 저장한다.
        const nodeToBePopped = this.tail;
        
        // 리스트의 Tail에 prev 속성이 존재하는 경우, 
        if (nodeToBePopped.prev) {
            this.tail = nodeToBePopped.prev; // 기존 Tail의 이전 노드를 새로운 Tail로 지정한다.

            this.tail.next = null; // 기존 Tail에 대한 참조를 제거한다.

            nodeToBePopped.prev = null; // [중요] 기존 Tail의 prev 속성을 null로 변경한다.
        } 
        // prev 속성이 존재하지 않으면, 리스트를 초기화한다.
        else {
            this.head = null;
            this.tail = null;
        }

        // 리스트의 길이를 감소시킨다.
        this.length--;

        // 삭제한 노드를 반환한다.
        return nodeToBePopped;
    }

    // O(1)
    shift() {
        // 리스트가 비어있다면 undefined를 반환한다.
        if (this.head === null) return;

        // 리스트의 현재 Head를 변수에 저장한다.
        const shiftedNode = this.head;

        // 제거할 노드의 next 속성이 존재하는 경우,
        if (shiftedNode.next) {
            this.head = shiftedNode.next; // 제거할 노드의 다음 노드를 Head로 설정한다.

            this.head.prev = null; // 새로 지정된 Head에서 기존 Head에 대한 참조를 제거한다.

            shiftedNode.next = null; // 제거될 노드의 next도 초기화한다.
        }
        // 제거할 요소가 리스트의 마지막 요소인 경우, 리스트롤 초기화한다.
        else {
            this.head = null;
            this.tail = null;
        }

        // 리스트의 길이를 감소시킨다.
        this.length--;

        return shiftedNode;
    }

    // O(1)
    unshift(newVal) {
        // 새로운 노드를 생성한다.
        const newNode = new Node(newVal);

        // 리스트가 비어있는 경우, Head와 Tail을 생성된 노드로 설정한다.
        if (this.head === null) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            newNode.next = this.head; // 생성된 노드의 next 값을 리스트의 Head로 설정한다.

            this.head.prev = newNode; // 기존 Head의 prev 값을 생성된 노드로 설정한다.

            this.head = newNode; // 리스트의 Head를 생성된 노드로 변경한다.
        }

        // 리스트의 길이를 증가시킨다.
        this.length++;
        
        return this;
    }

    // O(N) - 앞/뒤에서 탐색을 시작하도록 최적화하여 O(N/2)이지만, 여전히 O(N)이다.
    get(position) {
        // 리스트의 범위를 벗어난 경우, null을 반환한다.
        if (position < 0 || position >= this.length) return null;

        const middle = Math.floor(position / 2);
        let currentNode;
        let counter;

        // 중간값보다 작은 위치인 경우, 리스트의 앞에서 시작한다.
        if (position <= middle) {
            currentNode = this.head;  // Head 노드를 먼저 변수에 저장한다.
            counter = 0;              // counter를 0으로 설정한다.

            // // counter와 position이 같아지는 순간까지 반복한다.
            while (counter < position) {
                currentNode = currentNode.next;
                counter++;
            }
        }
        // 중간값보다 큰 위치인 경우, 리스트의 뒤에서 시작한다.
        else {
            currentNode = this.tail;    // Tail 노드를 먼저 변수에 저장한다.
            counter = this.length - 1;  // counter를 리스트의 길이 - 1로 설정한다.

            // counter와 position이 같아지는 순간까지 반복한다.
            while (counter > position) {
                currentNode = currentNode.prev;
                counter--;
            }
        }

        return currentNode;
    }

    // O(N)
    set(newVal, position) {
        // 앞서 구현한 get() 메서드를 이용해 위치에 해당하는 노드를 찾는다.
        const targetNode = this.get(position);

        if (targetNode) {
            targetNode.value = newVal;
            return true;
        } 

        // 위치에 해당하는 노드를 찾지 못한 경우, false를 반환한다.
        return false;
    }

    // O(N)
    insert(newVal, position) {
        if (position < 0 || position >= this.length) return false;
        if (position === 0) return !!this.unshift(newVal);
        if (position === this.length - 1) return !!this.push(newVal);

        const newNode = new Node(newVal);        // 새로운 노드를 생성한다.
        const prevNode = this.get(position - 1); // 삽입할 위치 이전 위치의 노드를 선택한다.
        const targetNode = prevNode.next;        // 삽입할 위치에 있는 노드를 선택한다.
        
        // 삽입할 노드 앞, 뒤 노드의 참조들을 변경한다.
        prevNode.next = newNode;
        newNode.prev = prevNode;
        newNode.next = targetNode;
        targetNode.prev = newNode;

        // 리스트의 길이를 증가시킨다.
        this.length++;

        return true;
    }

    // O(N)
    remove(position) {
        if (position < 0 || position >= this.length) return undefined;
        if (position === 0) return !!this.shift();
        if (position === this.length - 1) return !!this.pop();

        const prevNode = this.get(position - 1); // 삭제할 위치 이전 위치의 노드를 선택한다.
        const targetNode = prevNode.next;        // 삭제할 위치에 있는 노드를 선택한다.
        const nextNode = targetNode.next;        // 삭제할 위치 다음 위치의 노드를 선택한다.

        // 삭제할 노드에 대한 연결을 끊고, 앞, 뒤 노드를 연결한다.
        prevNode.next = nextNode;
        nextNode.prev = prevNode;

        // 삭제된 노드의 prev, next를 초기화한다.
        targetNode.prev = null;
        targetNode.next = null;

        // 리스트의 길이를 감소시킨다.
        this.length--;

        return targetNode;
    }
}

const DLL = new DoublyLinkedList();
DLL.push(1);
DLL.push(2);
DLL.push(3);
DLL.push(4);