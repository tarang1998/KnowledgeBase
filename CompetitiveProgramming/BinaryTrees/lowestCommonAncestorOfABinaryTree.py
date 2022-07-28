# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    ans = None
    
    
    def parseTree(self, node, p, q):
        
        if(node == None ):
            return 0
        
        leftTree = self.parseTree(node.left,p,q)
        
        if(leftTree == 2):
            return 2
        
        curr = 1 if (node == p or node == q) else 0 
        
        if(leftTree + curr == 2):
            self.ans = node
            return 2
        
        rightTree = self.parseTree(node.right,p,q)
        
        if(rightTree == 2):
            return 2
          
        if curr+leftTree+rightTree == 2:
            self.ans = node
            return 2
            
        return curr + leftTree + rightTree
        
      
        

        
        
        
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.ans = None
        
        self.parseTree(root,p,q)
        
        return self.ans
        
        
        
        
        
        