# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            if x.val != y.val:
                return False
            return isMirror(x.left, y.right) and isMirror(x.right, y.left)
        return isMirror(root.left, root.right)
