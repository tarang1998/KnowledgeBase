#https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:    
    
    def parseTree(self,node):
        
        if(node == None):
            return 0 
        
        leftSubtreeLength = self.parseTree(node.left)
        
        rightSubtreeLength = self.parseTree(node.right)
        
        if(leftSubtreeLength == -1 or rightSubtreeLength == -1):
            return -1
        
        if(leftSubtreeLength == rightSubtreeLength):
            return leftSubtreeLength + 1
        
        elif(leftSubtreeLength > rightSubtreeLength):
            
            if(leftSubtreeLength - rightSubtreeLength > 1):
                return -1 
            
            else:
                return leftSubtreeLength + 1
        
        else:
            if(rightSubtreeLength - leftSubtreeLength > 1):
                return -1 
            
            else:
                return rightSubtreeLength + 1
            
        
        
        
        
        
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return False if self.parseTree(root) == -1 else True 
        
        
         