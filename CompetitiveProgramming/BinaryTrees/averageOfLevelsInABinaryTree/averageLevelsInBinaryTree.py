# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def parseTree(self,node,level,totalSum,totalNodes):

        if(node == None):
            return

        if(len(totalSum) <= level):
            totalSum.append(node.val)
            totalNodes.append(1)
        else:
            totalSum[level] += node.val
            totalNodes[level] += 1

        self.parseTree(node.left,level+1,totalSum,totalNodes)
        self.parseTree(node.right,level+1,totalSum,totalNodes)






    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        totalSum = []

        totalNodes = []

        self.parseTree(root,0,totalSum,totalNodes)

        result = []

        for i in range(len(totalNodes)):

            result.append(totalSum[i]/totalNodes[i])

        return result



