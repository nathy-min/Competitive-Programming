# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = current = ListNode(-1)
        while l1 or l2:
            result = carry
            if l1:
                result += l1.val
                l1 = l1.next
            if l2:
                result += l2.val
                l2 = l2.next
            
            current.next = ListNode(result % 10)
            carry = result // 10
            
            current = current.next
        if carry:
            current.next = ListNode(carry)
        return head.next
