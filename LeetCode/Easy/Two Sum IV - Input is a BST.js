function preOrder(visited, node) {
    visited.push(node.val);
    if(node.left) preOrder(visited, node.left);
    if(node.right) preOrder(visited, node.right);
  }
  
  function DFS(root) {
    const visited = [];
    let current = root;
    
    // 전위 순회 함수를 호출한다.
    preOrder(visited, current);
    
    return visited;
  }
  
  function findValue(root, value) {
    if (!root) return false;
    
    let current = root;
    let found = false;
    
    while(current && !found) {
      if (value < current.val) current = current.left; // 왼쪽 자식 탐색
      else if (current.val < value) current = current.right; // 오른쪽 자식 탐색
      else found = true; // 목표한 노드를 찾으면, found를 true로 변경 
    }
    
    return found;
  }
  
  /**
   * Definition for a binary tree node.
   * function TreeNode(val, left, right) {
   *     this.val = (val===undefined ? 0 : val)
   *     this.left = (left===undefined ? null : left)
   *     this.right = (right===undefined ? null : right)
   * }
   */
  
  /**
   * @param {TreeNode} root
   * @param {number} k
   * @return {boolean}
   */
  const findTarget = function(root, k) {
    const nodeValues = DFS(root); // BST 노드들의 값을 DFS로 탐색해 배열로 반환
    let answer = false;
    
    for (const value of nodeValues) {
      const target = k - value; // 목표 값을 만들기 위해 필요한 수
      
      if (target === value) continue; // 같은 값을 두 번 사용하는 경우 제외

      // 목표 값을 만들기 위해 필요한 수가 BST에 존재하면, 반복문 종료
      if (findValue(root, target)) {
        answer = true;
        break;
      }
    }
    
    return answer;
  };