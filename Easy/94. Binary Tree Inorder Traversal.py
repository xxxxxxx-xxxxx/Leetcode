# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Hard problem, not good with this yet, the null means nothing there.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def order(node):
            if not node:
                return
            order(node.left)            # 1) left
            res.append(node.val)        # 2) node
            order(node.right)           # 3) right

        order(root)
        return res
  
