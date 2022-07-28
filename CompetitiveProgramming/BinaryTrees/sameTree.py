#https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def parseTrees(self, pnode, qnode):
        
        if((pnode == None) ^ (qnode == None)):
            return False
        
        if(pnode == None and qnode == None):
            return True 
        
        if(pnode.val != qnode.val):
            return False
        
        left = self.parseTrees(pnode.left,qnode.left)
        
        if(not(left)):
            return left
        
        right = self.parseTrees(pnode.right,qnode.right)
        
        if(not(right)):
            return right
        
        return True 
        
            
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        return self.parseTrees(p,q)
        