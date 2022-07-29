# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    result = {}
    
  
    def parseTree(self,node,level):
        
        if(node == None):
            return 
        
        if(level not in self.result):
            
            self.result[level] = [node.val]
            
        else:
            
            if(level % 2 == 0):
                self.result[level].append(node.val)
                
            elif(level % 2 == 1):
                self.result[level].insert(0,node.val)
                
        self.parseTree(node.left,level+1)
        
        self.parseTree(node.right, level+1)
        
            
            
        
        
        
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.result = {}
        
        self.parseTree(root,0)
        
        return list(self.result.values())
        
            
        
        

