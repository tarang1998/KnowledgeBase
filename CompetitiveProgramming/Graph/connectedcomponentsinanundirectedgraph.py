from collections import defaultdict

class Solution:
    def countComponents(self, n, edges):
        """
        Time Complexity: O(n + e) where n = number of nodes, e = number of edges
        Space Complexity: O(n + e) for the graph and visited set
        """

        # Step 1: Build the graph using adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # because the graph is undirected

        visited = set()  # Keeps track of visited nodes
        components = 0   # This will count the connected groups

        # Step 2: DFS function to explore one component
        def dfs(node):
            visited.add(node)  # Mark the node as visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)  # Visit all neighbors recursively

        # Step 3: Loop through all nodes
        for i in range(n):
            if i not in visited:
                dfs(i)           # New component found, start DFS
                components += 1  # Increase component count

        return components  # Total number of connected components
    



    def countComponentsUnionFind(self, n, edges):
        """
        Time Complexity: O(α(n)) ≈ O(1) per operation, total ~ O(n + e)
        Space Complexity: O(n) for parent and rank arrays
        """

        # Step 1: Initialize each node to be its own parent
        parent = [i for i in range(n)]
        rank = [1] * n  # Used to keep tree flat

        # Step 2: Define the find function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        # Step 3: Define the union function with union by rank
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False  # Already in the same group

            # Union by rank (attach smaller tree under bigger one)
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

            return True  # Union successful

        # Step 4: Process all edges
        components = n  # Start with all nodes as separate components
        for u, v in edges:
            if union(u, v):     # If union is successful, reduce component count
                components -= 1

        return components  # Final number of connected components



            




