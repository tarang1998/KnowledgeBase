
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Time Complexity : O(n) : n is the no of nodes in each tree. The algorithm will parse through each node in both of these trees
    # Space Complexity : O(n) :  In the worst case we get a full and complete binary trees
    # The number of leaves is L = (N + 1)/2 , where N is the no of nodes
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # Function to perform depth-first search and store the leaf nodes 
        def recurse(root, res):
            if not root:
                return
            if not root.left and not root.right:
                res.append(root.val)
            recurse(root.left, res)
            recurse(root.right, res)

        res1 = []
        res2 = []

        recurse(root1, res1)
        recurse(root2, res2)

        return res1 == res2


