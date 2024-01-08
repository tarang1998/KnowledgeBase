# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    # Time Complexity : O(n) Worst case possible incase all the nodes of the tree have to be visited 
    # Space Complexity : O(n) in the worst case
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if(root == None):
            return 0 

        totalSum = 0 

        # If condition satisfies add the value to totalSum
        if(low <= root.val and root.val <= high):
            totalSum += root.val

        if(root.val<high):
            totalSum += self.rangeSumBST(root.right,low,high)

        if(root.val > low):
            totalSum += self.rangeSumBST(root.left,low,high)

        return totalSum


        