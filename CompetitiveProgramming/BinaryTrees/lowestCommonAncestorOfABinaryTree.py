# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Time Complexity : O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        result = None 

        def traverse(node,p,q):
            nonlocal result 

            if node == None:
                return False 

            left = traverse(node.left,p,q)
            right = traverse(node.right,p,q)
            curr = (node.val == p.val) or (node.val == q.val)

            if (left and right) or (left and curr) or (right and curr):
                result = node

            return left or right or curr

        traverse(root,p,q)
        return result



           