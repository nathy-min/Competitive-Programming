# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        prev,cur = dummy,head
        while cur and cur.next:
            nxt = cur.next.next
            sec = cur.next
            cur.next=nxt
            sec.next=cur
            prev.next= sec
            
            prev = cur
            cur = nxt
            
        return dummy.next     