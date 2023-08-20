# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ""

        if(root == None):
            return result

        result += "{}".format(root.val)

        if(root.left != None):
            result += "({})".format(self.tree2str(root.left))
        else:
            if(root.right != None):
                result += "()"

        if(root.right != None):
            result += "({})".format(self.tree2str(root.right))

        return result
