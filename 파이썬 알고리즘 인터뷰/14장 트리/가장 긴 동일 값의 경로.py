# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # 자식 노드가 존재하고, 값이 같은 경우 자식 노드의 상태값을 1 증가시킨다.
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽, 오른쪽 자식 노드 사이의 거리가 최대가 되어야 한다.
            self.longest = max(self.longest, left + right)
            # 두 자식 노드 상태값 중 큰 것을 반환한다.
            return max(left, right)

        dfs(root)
        return self.longest
