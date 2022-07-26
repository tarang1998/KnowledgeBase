# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def parseTree(self,node,preorderTraversal):
        
        if (node == None):
            return 
        
        preorderTraversal.append(node.val)
        
        self.parseTree(node.left,preorderTraversal)
        
        self.parseTree(node.right,preorderTraversal)
    
    def preorderTraversal(self, root):
        
        preorderTraversal = []
        
        self.parseTree(root,preorderTraversal)
        
        return preorderTraversal
        
        
        
        
        
  