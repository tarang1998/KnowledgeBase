# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        mem = {}
        def dfs(node):
            if node is None:
                return False
            left = k - node.val
            if left in mem:
                return True
            mem[node.val] = 1 
            return dfs(node.left) or dfs(node.right)

        return dfs(root)

    def findTarget1(self, root: Optional[TreeNode], k: int) -> bool:
        def findMin(node):
            while node.left:
                node = node.left
            return node 

        def find(node,key):
            if node is None:
                return False
            if key < node.val:
                return find(node.left,key)
            elif key> node.val:
                return find(node.right,key)
            else:
                return True

            

        # Deletes the root 
        # And returns the new root
        def delete(node,key):
            if not node:
                return None

            if key < node.val:
                node.left = delete(node.left,key)
            elif key > node.val:
                node.right = delete(node.right,key)
            else: 
                #Key found 
                if node.left == None:
                    return node.right
                elif node.right == None:
                    return node.left
                else:
                    successor = findMin(node.right)
                    node.val = successor.val
                    node.right = delete(node.right,successor.val)
            return node 

        while root:
            target = k - root.val
            if find(root.left,target):
                return True
            elif find(root.right,target):
                return True
            else:
                root = delete(root,root.val)

        return False
       