# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        newnode = ListNode(0,head)
        left= newnode
        right = head
        while n > 0:
            right= right.next
            n -= 1
        while right:
            right = right.next
            left = left.next
            
        left.next = left.next.next    
        
        return newnode.next