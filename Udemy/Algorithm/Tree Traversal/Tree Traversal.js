class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BST {
    constructor() {
        this.root = null;
    }

    insert(value) {
        const newNode = new Node(value);

        if (!this.root) {
            this.root = newNode;
            return this;
        } 

        let currentNode = this.root;

        while (true) {
            if (value === currentNode.value) break;

            if (value > currentNode.value) {
                if (currentNode.right) {
                    currentNode = currentNode.right;
                } else {
                    currentNode.right = newNode;
                    break;
                }
            } else {
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

    find(value) {
        if (!this.root) return;

        let currentNode = this.root;

        while(true) {
            if (currentNode.value === value) return currentNode;

            if (value < currentNode.value) {
                if (!currentNode.left) return;
                currentNode = currentNode.left;
            } else {
                if (!currentNode.right) return;
                currentNode = currentNode.right;
            }
        }
    }

    BFS() {
        const visited = [];
        const queue = [this.root, ];

        // [주의] Javascript의 빈 배열은 Truthy Value이다.
        while (queue.length > 0) {
            const current = queue.pop();
            visited.push(current.value);

            if (current.left) queue.unshift(current.left);
            if (current.right) queue.unshift(current.right);
        }

        return visited;
    }

    // 전위 순회
    preOrder(visited, node) {
        visited.push(node.value);
        if (node.left) this.preOrder(visited, node.left);
        if (node.right) this.preOrder(visited, node.right);    
    }

    // 중위 순회
    inOrder(visited, node) {
        if (node.left) this.inOrder(visited, node.left);
        visited.push(node.value);
        if (node.right) this.inOrder(visited, node.right);    
    }

    // 후위 순회
    postOrder(visited, node) {
        if (node.left) this.postOrder(visited, node.left);
        if (node.right) this.postOrder(visited, node.right);
        visited.push(node.value);    
    }

    DFS(traversalMethod) {
        const visited = []
        let current = this.root;

        if (traversalMethod == "pre-order") this.preOrder(visited, current);
        if (traversalMethod == "in-order") this.inOrder(visited, current);
        if (traversalMethod == "post-order") this.postOrder(visited, current);
        
        return visited;
    }
}



const tree = new BST();
tree.insert(10);  // Binary Search Tree
tree.insert(6);   //
tree.insert(15);  //         10
tree.insert(3);   //      6      15
tree.insert(8);   //    3   8      20
tree.insert(20);  //

console.log(tree.BFS());             // [10, 6, 15, 3, 8, 20]
console.log(tree.DFS("pre-order"));  // [10, 6, 3, 8, 15, 20]
console.log(tree.DFS("in-order"));   // [3, 6, 8, 10, 15, 20]
console.log(tree.DFS("post-order")); // [3, 8, 6, 20, 15, 10]