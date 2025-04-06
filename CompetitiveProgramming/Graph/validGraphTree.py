from collections import defaultdict

class Solution:
    visited = None
    neighbors = None

    def dfs(self, parent, node):
        if node in self.visited:
                return False
        self.visited[node] = 1
        for neighbor in self.neighbors[node]:
            if neighbor == parent:
                continue            
            if not self.dfs(node, neighbor):
                return False
        return True 
            
    # Time Complexity : O(E+V)
    # Space Complexity : O(E+V)
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        self.visited = {}
        self.neighbors = defaultdict(list)

        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            self.neighbors[node1].append(node2)
            self.neighbors[node2].append(node1)

        # To be a valid tree, 
        # The graph should not have any cycles and must be connected
        return self.dfs(None,0) and len(self.visited) == n 
          

            

