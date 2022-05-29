# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        leng=0
        start = node = head
        while start:
            leng +=1
            start = start.next
        middle = leng//2
        counter=0
        while node:
            if counter == middle:
                return node
            else:
                counter +=1
                node = node.next
        return None         