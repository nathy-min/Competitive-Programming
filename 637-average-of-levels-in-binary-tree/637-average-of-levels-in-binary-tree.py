# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = []
        q = deque([root])
        
        while q:
            total_sum=sum([a.val for a in q]) 
            avg = total_sum/len(q)
            level.append(avg)
            for i in range(len(q)):
                n= q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right) 
            
        return level    