# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    ans = - float('inf') 
    
    
    def parseTree(self, node):
        
        if(node == None):
            return 0 
        
        left = self.parseTree(node.left)
        
        right = self.parseTree(node.right)
        
    
        #Variable signifying the max path from this node 
        value = max(node.val,node.val+left,node.val +right)
            
        nodePathSum = node.val + left + right
        

        if( max(value,nodePathSum) > self.ans ):
            self.ans = max(value,nodePathSum)
        
        return value
        
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = - float('inf') 
        
        self.parseTree(root)
        
        return self.ans
        
        
        