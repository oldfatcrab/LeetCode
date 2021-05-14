# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> (TreeNode, TreeNode):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return (None, None)
        (leftHead, leftTail), (rightHead, rightTail) = self.flatten(root.left), self.flatten(root.right)
        if not leftHead:
            return (root, rightTail or root)
        root.left, root.right = None, leftHead
        if rightHead:
            leftTail.right = rightHead
        return (root, rightTail or leftTail)