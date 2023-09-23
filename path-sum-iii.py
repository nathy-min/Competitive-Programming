# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, pre_sum):
            nonlocal no_path
            nonlocal dic
            if not node:
                return
            pre_sum += node.val
            if pre_sum == targetSum:
                no_path += 1
            no_path += (dic[pre_sum - targetSum])
            dic[pre_sum] += 1    

            dfs(node.left, pre_sum)
            dfs(node.right, pre_sum)
            dic[pre_sum] -= 1

        no_path = 0
        dic = defaultdict(int)
        dfs(root,0)
        return no_path