import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS를 이용한 Top to Bottom (Runtime: 24ms, Memory: 14MB)
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root

    # DFS를 이용한 Top to Bottom (Runtime: 24ms, Memory: 14MB)
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque()
        stack.append(root)

        while stack:
            node = stack.pop()

            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root