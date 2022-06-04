# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        length = 0
        h = head
        while h:
            length += 1
            h = h.next
        answer = [0] * length
        temp = []
        stack = []
        while head:
            while stack and head.val > temp[stack[-1]]:
                answer[stack.pop()] = head.val
            temp.append(head.val)
            stack.append(len(temp) - 1)
            head = head.next
        return answer   