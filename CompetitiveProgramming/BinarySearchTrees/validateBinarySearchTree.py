# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def parseTree(node,maxValue,minValue):
        
            if(node == None):
                return True

            if(node.val >= maxValue or node.val <= minValue ):
                return False

            return parseTree(node.left,node.val,minValue) and parseTree(node.right,maxValue,node.val)
        
        return parseTree(root,float('inf'),-float('inf'))
        
        