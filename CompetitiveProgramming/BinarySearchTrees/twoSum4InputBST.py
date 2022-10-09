#https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    


    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        encounteredValues = {}

        def inorderTraveral(node):

            if(node == None):
                return

            inorderTraveral(node.left)

            if(node.val in encounteredValues):
                encounteredValues[node.val] += 1
            else:
                encounteredValues[node.val] = 1

            inorderTraveral(node.right)



        inorderTraveral(root)

        for key,value in encounteredValues.items():

            reqVal = k - key

            if (reqVal == key):
                if(encounteredValues[key] == 2):
                    return True
            else:
                if( reqVal in encounteredValues):
                    return True
        
        return False





