# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         current = head
#         prev = None
        
#         while current:
#             tmp_next = current.next
#             current.next = prev
#             prev = current
#             current = tmp_next
#         return prev
        
        
        #### Recursive
        
        if (not head) or (not head.next):
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return p
