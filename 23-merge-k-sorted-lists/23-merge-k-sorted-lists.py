# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        al = []
        start = end = ListNode(-1)
        for i in lists:
            while i:
                al.append(i.val)
                i = i.next
        for j in sorted(al):
            n = ListNode(j)
            end.next = n 
            end = n
        return start.next