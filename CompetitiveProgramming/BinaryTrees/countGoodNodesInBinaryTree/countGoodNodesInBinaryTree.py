# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    goodNodesCount = 0

    def parse(self,node,maxValue):

        if(node == None):
            return

        if(node.val >= maxValue):
            self.goodNodesCount += 1
            maxValue = node.val

        self.parse(node.left,maxValue) 

        self.parse(node.right,maxValue)

    



    def goodNodes(self, root: TreeNode) -> int:

        self.parse(root,-100000)

        return self.goodNodesCount

        