# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = head
        while dummy:
            while dummy.next and dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            dummy = dummy.next
            
        return head      