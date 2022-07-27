# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    
    
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    
    solution = []
    
    def parseTree(self,node,target):
        
        if(node == None):
            return False
            
        if(node.val == target):
            self.solution.append(node.val)
            return True
            
        r1 = self.parseTree(node.left,target)
        
        if(r1):
            self.solution.insert(0,node.val)
            return True
            
        r2 = self.parseTree(node.right,target)
        
        if(r2):
            self.solution.insert(0,node.val)
            return True
            
    
        
    
    def solve(self, A, B):
        
        self.solution = []
        
        self.parseTree(A,B)
        
        return self.solution
        
        
        
        
