# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True          # If both are empty
        if not p or not q:
            return False         # If one is empty
        if p.val != q.val:
            return False         # If different value
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Could actually make a little more compat by doing
class Solution:
    def isSameTree(self, p, q):
        if not p or not q:
            return p is q
        return (p.val == q.val 
                and self.isSameTree(p.left, q.left) 
                and self.isSameTree(p.right, q.right))
