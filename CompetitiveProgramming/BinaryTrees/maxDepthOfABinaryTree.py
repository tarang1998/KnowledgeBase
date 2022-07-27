#https://leetcode.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    maxDepth = 0 
    
    
    def parseTree(self,node,level):
        
        if(node == None):
            return
        
        if(level > self.maxDepth):
            self.maxDepth = level
            
        self.parseTree(node.left, level+1)
        
        self.parseTree(node.right, level+1)
        
        
        
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.maxDepth = 0 
        
        self.parseTree(root,1)
        
        return self.maxDepth
        
        
        