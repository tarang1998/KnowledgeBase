# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    
    def parseTree(self,treeNode):
        
        if(treeNode == None):
            return None
        
        leftNode = treeNode.left
        
        rightNode = treeNode.right
        
        
        if (leftNode != None):
            
            treeNode.left = None
            
            #parse till the rightmost node of the left subtree
            temp = leftNode     
            
            while(temp.right != None):
                
                temp = temp.right
                
            temp.right = rightNode
            
            treeNode.right = leftNode
        
        
        self.parseTree(treeNode.right)
        
        return treeNode
        
            
            
        
       
        
                  
    def flatten(self, root):
        
        return self.parseTree(root)
        
    
        
        
        