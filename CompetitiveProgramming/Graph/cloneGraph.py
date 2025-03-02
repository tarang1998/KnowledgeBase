#https://leetcode.com/problems/clone-graph/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    # Time Complexity : O(E+V)
    # Space Complexity : O(V)
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNewNodeMapping = {}

        def dfs(node):

            if node in oldToNewNodeMapping:
                return oldToNewNodeMapping[node]

            copy = Node(node.val)
            oldToNewNodeMapping[node] = copy

            for neighbors in node.neighbors:
                copy.neighbors.append(dfs(neighbors))

            return copy
        
    
        def bfs(node):

            q = deque()
            q.append(node)

            oldToNewNodeMapping[node] = Node(node.val)

            while q:
                cur = q.popleft()

                for neighbor in cur.neighbors:
                    if neighbor not in oldToNewNodeMapping:
                        oldToNewNodeMapping[neighbor] = Node(neighbor.val)
                        q.append(neighbor)
                    oldToNewNodeMapping[cur].neighbors.append(oldToNewNodeMapping[neighbor])

            return oldToNewNodeMapping[node]

        


        #return dfs(node) if node else None
        return bfs(node) if node else None 
        
        
    
        
        