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
        dum= ListNode()
        tail = dum
        l1= list1
        l2= list2
        while l1 and l2:
            if l1.val < l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next = l2
                l2= l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next= l2
        return dum.next    