# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            # 리프 노드에서 호출된 경우, 상태값으로 -1을 반환
            if not node:
                return -1

            l_state = dfs(node.left)   # 왼쪽 자식 노드의 상태값
            r_state = dfs(node.right)  # 오른쪽 자식 노드의 상태값

            self.longest = max(self.longest, l_state + r_state + 2)
            return max(l_state, r_state) + 1  # 현재 노드의 상태값

        dfs(root)
        return self.longest
