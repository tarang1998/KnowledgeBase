# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def findSolution(self,preorder,inorder):
        
        if(len(preorder) == 0 or len(inorder) == 0):
            return None
        
        #find the root element 
        root = TreeNode()
        
        root.val = preorder[0]
        
        index = inorder.index(root.val)
        
        inorderleftSubTree = inorder[0:index]
        
        inorderrightSubTree = inorder[index+1:]
        
        preorderleftSubTree = preorder[1:len(inorderleftSubTree)+1]
        
        preorderrightSubTree = preorder[len(inorderleftSubTree)+1:]
        
        root.left = self.findSolution(preorderleftSubTree,inorderleftSubTree)
        
        root.right = self.findSolution(preorderrightSubTree,inorderrightSubTree)
        
        return root 
        
    
    
    def buildTree(self, preorder, inorder):
        
        root = self.findSolution(preorder,inorder)

        return root 
        