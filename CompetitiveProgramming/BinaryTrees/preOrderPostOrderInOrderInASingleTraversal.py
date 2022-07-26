#https://www.codingninjas.com/codestudio/problems/981269


# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
        
def parseTree(node,inorderTraversal,preOrderTraversal,postOrderTraversal):
    
    if(node == None):
        return
    
    preOrderTraversal.append(node.data)
    
    parseTree(node.left,inorderTraversal,preOrderTraversal,postOrderTraversal)
    
    inorderTraversal.append(node.data)
    
    parseTree(node.right,inorderTraversal,preOrderTraversal,postOrderTraversal)
    
    postOrderTraversal.append(node.data)
    
    return
    
    
    
    
    

def getTreeTraversal(root):
    # Write your code here.
    
    inorderTraversal = []
    
    postOrderTraversal = []
    
    preOrderTraversal = []
    
    parseTree(root,inorderTraversal,preOrderTraversal,postOrderTraversal)
    
    return [inorderTraversal,preOrderTraversal,postOrderTraversal]

