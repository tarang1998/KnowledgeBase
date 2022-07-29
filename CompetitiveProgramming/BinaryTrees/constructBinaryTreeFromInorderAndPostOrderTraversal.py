#https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    
    def constructTree(self,inorder,postorder):
        
        if(len(inorder) == len(postorder) == 0 ):
            return None
                
        if(len(inorder) == len(postorder) == 1 ):
            
            node = TreeNode()
            node.left = None
            node.right = None
            node.val = inorder[0]
            return node 
        
        root = postorder[-1]
        
        
        # inorder
        inorderRootIndex = inorder.index(root)

        leftTreeInorder = inorder[0:inorderRootIndex]
        
        rightTreeInorder = inorder[inorderRootIndex+1:]
        
        
        #postorder 
        leftTreePostOrder = postorder[0:len(leftTreeInorder)]
        rightTreePostOrder = postorder[len(leftTreeInorder):len(postorder)-1]
        
        
        node = TreeNode()
        node.val = root
        node.left = self.constructTree(leftTreeInorder,leftTreePostOrder)
        node.right = self.constructTree(rightTreeInorder,rightTreePostOrder)
        
        return node
        
        
    
        
        
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.constructTree(inorder,postorder)
        