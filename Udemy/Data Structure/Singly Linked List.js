class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(value) {
        // 1. 새로운 노드를 생성한다.
        const newNode = new Node(value);

        // 2. 리스트의 Head가 비어있는 경우, Head와 Tail을 새로 생성된 노드로 설정한다.
        if (this.head === null) {
            this.head = newNode;
            this.tail = newNode;
        } 
        // 3. 그렇지 않다면 Tail 뒤에 새로운 노드를 붙이고, 그 노드를 Tail로 설정한다.
        else {
            this.tail.next = newNode;
            this.tail = newNode;
        }

        // 4. 리스트의 길이를 증가시킨다.
        this.length++;

        return this;
    }

    pop() {
        // 1. 리스트가 비어있는 경우, undefined를 반환한다.
        if (this.length === 0) return;

        let current = this.head;
        let secondLast;

        // 2. Tail의 이전 노드를 찾을 때까지 반복문을 수행한다.
        while (current.next) {
            secondLast = current;
            current = current.next;
        }

        // 3. 마지막에서 두번째 노드에서 다음 노드에 대한 참조를 끊는다.
        secondLast.next = null;
        // 4. Tail을 마지막에서 두번째 노드로 변경한다.
        this.tail = secondLast;
        // 5. 리스트의 길이를 감소시킨다.
        if (this.length === 1) {
            this.head = null;
            this.tail = null;
        }
        this.length--;

        // 6. 제거된 노드를 반환한다.
        return current;
    }

    shift() {
        // 1. 리스트가 비어있는 경우, undefined를 반환한다.
        if (this.head === null) return;
        
        // 2. 현재의 Head를 별도의 변수에 저정한다.
        const currentHead = this.head;

        // 3. 리스트의 Head를 현재 Head의 다음 노드로 변경한다.
        this.head = currentHead.next;

        // 4. 길이를 감소시킨다.
        if (this.length === 1) {
            this.tail = null;
        }
        this.length--;

        // 5. 제거된 노드를 반환한다.
        return currentHead;
    }

    unshift(value) {
        // 1. 새로운 노드를 생성한다.
        const newNode = new Node(value);

        // 2. 리스트가 비어있는 상태라면, Head와 Tail을 새로운 노드로 설정한다.
        if (this.head === null) {
            this.head = newNode;
            this.tail = newNode;
        }
        // 3. 그렇지 않다면, 새로운 노드의 다음 노드로 현재의 Head를 설정한다.
        else {
            newNode.next = this.head;

            // 4. 리스트의 Head를 새로운 노드로 변경한다.
            this.head = newNode;
        }

        // 5. 길이를 증가시킨다.
        this.length++;

        return this;
    }

    get(position) {
        // 1. 주어진 위치값이 범위를 벗어나는 경우 null을 반환한다.
        if (position < 0 || position >= this.length) return null;
        
        let counter = 0;
        let current = this.head;

        // 2. 리스트를 순환하여 해당 위치의 노드에 접근한다.
        while (counter < position) {
            current = current.next;
            counter++;
        }

        // 3. 해둥 위치의 노드를 반환한다.
        return current;
    }

    set(value, position) {
        // 1. get() 메서드를 사용해 노드를 가져온다.
        const foundNode = this.get(position);

        // 2. 노드를 찾는데 실패한 경우, false를 반환한다.
        if (!foundNode) {
            return false;
        }
        // 3. 노드를 찾는데 성공한 경우, 노드의 값을 변경하고 true를 반환한다.
        else {
            foundNode.value = value;
            return true;
        }
    }

    insert(value, position) {
        // 1. 삽입할 위치가 범위를 벗어나는 경우, false를 반환한다.
        if (position < 0 || position >= this.length) return false;
        // 2. 삽일할 위치가 0인 경우, unshift() 메서드를 이용한다.
        if (position === 0) return !!this.unshift(value);
        // 3. 삽입할 위치가 리스트의 맨 끝인 경우, push() 메서드를 이용한다.
        if (position === this.length - 1) return !!this.push(value);

        // 4. 그 외의 경우, get() 메서드로 삽입할 위치 바로 앞의 노드를 가져온다.
        const newNode = new Node(value);
        const prevNode = this.get(position - 1);
        
        newNode.next = prevNode.next;
        prevNode.next = newNode;
        
        // 5. 길이를 증가시킨다.
        this.length++;
        
        return true;
    }

    remove(position) {
        // 1. 삭제할 위치가 범위를 벗어나는 경우, undefined를 반환한다.
        if (position < 0 || position >= this.length) return;
        // 2. 삭제할 위치가 리스트의 맨 앞인 경우, shift() 메서드를 이용한다.
        if (position === 0) return this.shift();
        // 3. 삭제할 위치가 리스트의 맨 끝인 경우, pop() 메서드를 이용한다.
        if (position === this.length - 1) return this.pop();

        // 4. 그 외의 경우, get() 메서드로 삭제할 위치 바로 앞의 노드를 가져온다.
        const prevNode = this.get(position - 1);
        const targetNode = prevNode.next;
        const nextNode = targetNode.next;
        
        prevNode.next = nextNode;
        
        // 5. 길이를 감소시킨다.
        this.length--;
        
        return targetNode;
    }

    reverse() {
        // 1. Head와 Tail을 바꾼다.
        let node = this.head;
        this.head = this.tail;
        this.tail = node;

        // 2. 현재 Node의 이전 노드와 다음 노드를 저장할 변수를 선언한다.
        let prevNode = null;
        let nextNode;

        for (let idx = 0; idx < this.length; i++) {
            // 3. 현재 노드의 다음 노드를 nextNode 변수에 저장한다.
            nextNode = node.next;
           
            // 4. 현재 노드의 다음 노드를 이전 노드로 변경한다.
            node.next = prevNode;            

            // 5. 다음 노드 처리를 위해 한 칸 이동한다.
            prevNode = node;
            node = nextNode;
        }

        return this;
    }
}