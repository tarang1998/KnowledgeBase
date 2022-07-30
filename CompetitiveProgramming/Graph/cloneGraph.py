#https://leetcode.com/problems/clone-graph/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    # key - value of the node 
    # value - the Node 
    visited = {}
    
    def constructGraph(self,node):
        
        if(node == None):
            return None
        
        if(node.val in self.visited):
            return self.visited[node.val]
        
        newNode = TreeNode()
        newNode.val = node.val
        newNode.neighbors = []
        
        self.visited[node.val] = newNode 
        
        for i in node.neighbors:
            
            newNode.neighbors.append(self.constructGraph(i))
        
        return newNode
        
        
        
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        self.visited = {}
        
        return self.constructGraph(node)
        