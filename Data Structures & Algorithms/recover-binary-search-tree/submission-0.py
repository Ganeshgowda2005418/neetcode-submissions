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
        res=[]
        def inorder(Node):
            if not Node:
                return 
            inorder(Node.left)
            res.append(Node)
            inorder(Node.right)
        inorder(root)
        Node1,Node2=None,None
        for i in range(len(res)-1):
            if res[i].val>res[i+1].val:
                Node2=res[i+1]
                if Node1 is None:
                    Node1=res[i]
                else:
                    break
        Node1.val,Node2.val=Node2.val,Node1.val
        