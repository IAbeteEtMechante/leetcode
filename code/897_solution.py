# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        sentinel = TreeNode(None)
        curr = sentinel
        
        node, stack = root, []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left = None
            curr.right = node
            curr = node
            node = node.right
        return sentinel.right
