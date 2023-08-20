# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def parseTree(self,treeNode,subRootNode):

        if((treeNode != None) ^ (subRootNode != None)):
            return False

        if(treeNode == None and subRootNode == None):
            return True

        return ((treeNode.val == subRootNode.val) and self.parseTree(treeNode.left, subRootNode.left) and self.parseTree(treeNode.right, subRootNode.right))

    

    def isSubtreeDFS(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if(root == None):
            return False

        if(subRoot == None):
            return True

        if(self.parseTree(root,subRoot)):
            return True

        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))


    def traverse(self,node):
        if(node):
            return "#{0} {1} {2}".format(node.val,self.traverse(node.left),self.traverse(node.right))
        return None


    def isSubtree(self, root : Optional[TreeNode], subRoot : Optional[TreeNode])-> bool:
        treeString = self.traverse(root)

        subTreeString = self.traverse(subRoot)

        if subTreeString in treeString:
            return True 

        return False

