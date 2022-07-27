# https://leetcode.com/problems/maximum-width-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    # key : node level
    # value : [ min index , max index]
    
    solution = {}

 
    def parseTree(self,node,level,index):
        
        if(node == None):
            return
        
        if(level not in self.solution):
            
            val = [float('inf'),-1]
            
            if(val[0] > index):
                val[0] = index
            
            if(val[1] < index):
                val[1] = index
                
            self.solution[level] = val
            
        
        else:
            
            val = self.solution[level]
            
            if(val[0] > index):
                val[0] = index
            
            if(val[1] < index):
                val[1] = index
                
                
            self.solution[level] = val
            
            
        self.parseTree(node.left,level+1,index*2+1)
        
        self.parseTree(node.right,level+1,index*2 +2)

        
        
    def widthOfBinaryTree(self, root):
        
        self.solution = {}
        
        maxDistance = 0 
        
        self.parseTree(root,0,0)
                
        for key,value in self.solution.items():
            
            leftDistance = value[0]
            
            rightDistance = value[1]
                
            distance = rightDistance - leftDistance + 1
            
            if(distance > maxDistance):
                
                maxDistance = distance
            
        return maxDistance
            
        
        
        
        
        
        
        