# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root, i = TreeNode(preorder[0]), inorder.index(preorder[0])
        root.left, root.right = self.buildTree(preorder[1:1 + i], inorder[:i]), self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return root