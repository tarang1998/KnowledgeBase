# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    diameter = 0 
    
    
    def parseTree(self,node):
        
        if(node == None):
            return 0
        
        
        leftSubtreeLength = self.parseTree(node.left)
        
        rightSubtreeLength = self.parseTree(node.right)
        
        length = leftSubtreeLength + rightSubtreeLength
        
        if(length == 0):
            return 1
        
        if(length > self.diameter):
            
            self.diameter = length
        
        if(leftSubtreeLength > rightSubtreeLength):
            return leftSubtreeLength + 1
        else:
            return rightSubtreeLength + 1
            
        
            
        
        
    
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0 
        
        self.parseTree(root)
        
        return self.diameter
        
        
        