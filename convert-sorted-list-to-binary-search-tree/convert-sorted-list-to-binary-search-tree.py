# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        
        dummy = ListNode(0)
        dummy.next, fast, slow = head, head, dummy
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            
        temp, slow.next = slow.next, None
        root = TreeNode(temp.val)
        root.left, root.right = self.helper(head), self.helper(temp.next)
        return root
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.helper(head)