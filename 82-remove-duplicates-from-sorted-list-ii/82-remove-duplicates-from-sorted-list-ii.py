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
        dummy = ListNode(0,head)
        
        back, front = dummy,head
        while front:
            if front.next and front.val == front.next.val:
                while front.next and front.val == front.next.val:
                    front = front.next
                back.next= front.next
            else:
                back = back.next
            front = front.next    
            
        return dummy.next  
        