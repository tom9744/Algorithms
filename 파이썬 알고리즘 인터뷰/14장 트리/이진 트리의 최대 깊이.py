from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 예외처리
        if root is None:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            # BFS 호출 횟수는 트리의 깊이에 따라 1씩 증가한다.
            depth += 1

            # 동일한 레벨에 있는 노드에 대해 다음을 수행한다.
            for _ in range(len(queue)):
                current_root = queue.popleft()

                # 자식 노드가 존재하는 경우, 큐에 추가한다.
                if current_root.left:
                    queue.append(current_root.left)
                if current_root.right:
                    queue.append(current_root.right)

        return depth
