# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tsum = 0
        def dfs(node):
            nonlocal tsum
            if not node:
                return 0
            lsum,rsum = dfs(node.left),dfs(node.right)
            tsum+= abs(lsum-rsum)
            return node.val + lsum + rsum
        dfs(root)
        return tsum