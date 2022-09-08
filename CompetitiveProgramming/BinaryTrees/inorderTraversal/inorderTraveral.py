# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def parseTree(self,node,inorderTraversal):
        
        if(node == None):
            return 
        
        self.parseTree(node.left,inorderTraversal)
        
        inorderTraversal.append(node.val)
        
        self.parseTree(node.right,inorderTraversal)
         
        
        
    
    def inorderTraversal(self, root):
        
        inorderTraversal = []
        
        self.parseTree(root,inorderTraversal)
        
        return inorderTraversal
        
        
        