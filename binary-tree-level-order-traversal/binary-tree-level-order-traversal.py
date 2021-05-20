# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        curr, result = [root], []
        while curr:
            currResult, nexts = [], []
            for node in curr:
                if node == None:
                    continue
                currResult.append(node.val)
                nexts += [node.left, node.right]
            if currResult:
                result.append(currResult)
            curr = nexts
        return result