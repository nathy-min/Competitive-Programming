# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prevele  = TreeNode(float("-inf"))
        drops = []
        def findPred(node):
            cur = node.left
            while cur.right and cur.right!= node:
                cur = cur.right
            return cur
        while root:
            if not root.left:
                if prevele.val > root.val:
                    drops.append((prevele,root))
                prevele = root
                root = root.right
            else:
                pre = findPred(root)
                if not pre.right:
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    if prevele.val > root.val:
                        drops.append((prevele,root))
                    prevele = root
                    root = root.right
                    #Why even live ffs I dont remember consentin to be born for this shit
        drops[0][0].val,drops[-1][1].val = drops[-1][1].val,drops[0][0].val