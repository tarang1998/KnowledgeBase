# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        currNode = root

        stack = []

        count = 0 

        while(True):

            if(currNode == None):
                node = stack.pop()
                count += 1

                if(count == k):
                    return node.val

                currNode = node.right

            else:

                stack.append(currNode)

                currNode = currNode.left


        




