# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    maxLevelReached = None  
    
    solution = []
    
    def parseTree(self,node,level):
        
        if(node == None):
            return
        
        if (self.maxLevelReached < level):
            
            self.solution.append(node.val)
            self.maxLevelReached  = level
            
        self.parseTree(node.right,level+1)
        self.parseTree(node.left,level+1)
            
        
    
    
    def rightSideView(self, root):
        
        self.solution = []
        
        self.maxLevelReached = 0 
        
        self.parseTree(root,1)
        
        return self.solution
        
        
            
            