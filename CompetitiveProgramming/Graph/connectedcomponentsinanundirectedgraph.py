from collections import defaultdict

class Solution:

    # Using Union - Find
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Keeping a record of parents of each node 
        # Initially each node is its own parent 
        parent = [node for node in range(n)]

        # No of nodes in the connected component
        # The root of a graph would have a rank equal to no of connected nodes  
        rank = [1 for node in range(n)]

        # Finding the parent of the node 
        def find(node):

            # Looping till the root node is found 
            while parent[node]!=node:
                parent[node] = parent[parent[node]] # Path compression to reach the root faster
                node = parent[node]
            
            return node 
        
        def union(node1,node2):

            # Finding the root of each parent 
            root1 = find(node1)
            root2 = find(node2)

            # if the roots are the same , they belong to the same connected graph
            # no new graph component is found , returning 0 
            if root1 == root2:
                return 0 
            
            # Increasing the rank and assigning as parent based on the root with the larger rank 
            # New graph component found, returning 1
            if rank[root2] > rank[root1]:
                parent[root1] = root2
                rank[root2] += rank[root1]
            else:
                parent[root2] = root1
                rank[root1] += root2
            return 1 
        
        result = n 

        for node1,node2 in edges:
            res -= union(node1, node2)

        return result 


            





    # Time Complexity : O(E+V)
    # Space Complexity : O(E+V)
    def countComponentsDFS(self, n: int, edges: List[List[int]]) -> int:

        neighbors = defaultdict(list)
        visited = {}

        count = 0 

        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
        
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)


        def dfs(node):

            if node in visited:
                return 
            
            visited[node] = 1

            for neighbor in neighbors[node]:
                dfs(neighbor)


        for node in range(n):
            if node in visited:
                continue 
            else:
                count += 1 
                dfs(node)
                

        return count 


        