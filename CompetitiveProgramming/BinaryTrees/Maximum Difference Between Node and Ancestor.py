# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Time Complexity : O(n)
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.maxDiff = 0 

        #Perform a depth first search and pass the min Value and the maxValue encountered
        #to calculate the maximum diff between the ancestor and the node 
        def recurse(node,minValue,maxValue):

            if not node:
                return

            self.maxDiff = max(self.maxDiff,abs(minValue-node.val),abs(maxValue - node.val))
            minValue = min(minValue,node.val)
            maxValue = max(maxValue,node.val)

            recurse(node.left, minValue, maxValue)
            recurse(node.right, minValue,maxValue)


        recurse(root,root.val,root.val)

        return self.maxDiff

        