# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def parseTree(self,node,postOrderTraversal):
        
        if (node == None):
            return
        
        self.parseTree(node.left,postOrderTraversal)
        
        self.parseTree(node.right,postOrderTraversal)
        
        postOrderTraversal.append(node.val)
        
        
        
        
    
    def postorderTraversal(self, root):
        
        postOrderTraversal = []
        
        self.parseTree(root,postOrderTraversal)
        
        return postOrderTraversal
                           
                           
        