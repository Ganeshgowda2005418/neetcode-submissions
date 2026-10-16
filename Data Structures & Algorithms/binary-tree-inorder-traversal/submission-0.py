# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(Node):
            if not Node:
                return None
            dfs(Node.left)
            res.append(Node.val)
            dfs(Node.right)
        dfs(root)
        return res