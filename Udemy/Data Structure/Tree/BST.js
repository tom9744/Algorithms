class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

/**
 * Insertion: O(logN)
 * Searching: O(logN)
 * 
 * 하지만 "정렬된 데이터가 트리에 입력되는" 최악의 경우, O(logN)이 보장되지 않는다.
 * 
 * 예를 들어, [1, 2, 3, 4, 5]와 같이 정렬된 데이터가 트리에 삽입되면 
 * 트리는 "단방향 연결 리스트"의 형태를 띄게 되며, 따라서 O(N)의 시간이 소요된다.
 */
class BST {
    constructor() {
        this.root = null;
    }

    // O(logN) - 반복문을 한 번 순회할 때마다, 데이터 수가 절반으로 줄어든다.
    insert(value) {
        const newNode = new Node(value);

        // 트리가 비어있는 경우, 생성한 노드를 루트로 지정한다.
        if (!this.root) {
            this.root = newNode;
            return this;
        } 

        let currentNode = this.root;

        while (true) {
            // 중복된 값이 들어온 경우, 무시한다.
            if (value === currentNode.value) break;

            // 새로운 값이 현재 위치의 값보다 크다면, 오른쪽으로 이동한다.
            if (value > currentNode.value) {
                if (currentNode.right) {
                    currentNode = currentNode.right;
                } else {
                    currentNode.right = newNode;
                    break;
                }
            }
            // 새로운 값이 현재 위치의 값보다 작다면, 왼쪽으로 이동한다. 
            else {
                if (currentNode.left) {
                    currentNode = currentNode.left;
                } else {
                    currentNode.left = newNode;
                    break;
                }
            }
        }

        return this;
    }

    // O(logN) - 반복문을 한 번 순회할 때마다, 데이터 수가 절반으로 줄어든다.
    find(value) {
        if (!this.root) return;

        let currentNode = this.root;

        while(true) {
            // 일치하는 노드를 발견한 경우, 해당 노드를 반환한다.
            if (currentNode.value === value) return currentNode;2

            // 값에 따라 이어서 탐색할 노드를 정한다. 노드가 존재하지 않으면 종료한다.
            if (value < currentNode.value) {
                if (!currentNode.left) return;
                currentNode = currentNode.left;
            } else {
                if (!currentNode.right) return;
                currentNode = currentNode.right;
            }
        }
    }

}

const tree = new BST();
