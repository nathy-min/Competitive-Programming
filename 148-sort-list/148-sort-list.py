# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        ary = []
        if node:
            while node.next:
                ary.append(node.val)
                node = node.next
            ary.append(node.val)
            node = head
            ary.sort()
            for i in ary:
                node.val = i
                node = node.next
        return head