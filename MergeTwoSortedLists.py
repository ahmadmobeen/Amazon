# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prehead = ListNode(-1)
        prev = prehead
        
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
            
        prev.next = list1 if list1 else list2
        
        return prehead.next
                
#         p = list1
#         q = list2

#         new = dummHead = ListNode(0)
#         while q or p:
#             if q and p:
#                 if q.val >= p.val:
#                     new.next = ListNode(p.val)

#                     new = new.next

#                     p = p.next
#                 else:
#                     new.next = ListNode(q.val)

#                     q = q.next
#                     new = new.next

#             else:
#                 if q:
#                     new.next = ListNode(q.val)
#                     q = q.next
#                     new = new.next
                    

#                 elif p:
#                     new.next = ListNode(p.val)

#                     p = p.next
#                     new = new.next
#         return dummHead.next
