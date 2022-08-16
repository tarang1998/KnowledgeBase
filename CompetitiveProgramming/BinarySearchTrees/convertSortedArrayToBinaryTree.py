# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if(len(nums)== 0 ):
            return None
        
        arrayMid = len(nums)//2
        
        leftSubtreeElements = nums[: arrayMid]
        
        rightSubtreeElements = nums[arrayMid + 1 :]
        
        root = TreeNode()
        
        root.val = nums[arrayMid]
        
        root.left = self.sortedArrayToBST(leftSubtreeElements)
        
        root.right = self.sortedArrayToBST(rightSubtreeElements)
        
        return root
        
        
       
        
        
      

            
            
            
        
       