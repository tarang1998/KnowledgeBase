# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def parseTree(self,node,p,q):

        if(p.val == node.val):
            return node

        if(q.val == node.val):
            return node 

        if(p.val < node.val and q.val < node.val):
            return self.parseTree(node.left,p,q)

        if(p.val > node.val and q.val > node.val):
            return self.parseTree(node.right,p,q)

        else:
            return node 


        

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        return self.parseTree(root,p,q)
        