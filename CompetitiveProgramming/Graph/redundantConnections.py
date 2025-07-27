class Solution:
    def findRedundantConnection(self, edges):
        """
        Time Complexity: O(n)
        Space Complexity: O(n) for parent and rank arrays
        """

        n = len(edges)
        parent = [i for i in range(n + 1)]  # parent[i] = leader of i's group
        rank = [1] * (n + 1)                # used to keep the tree flat for optimization

        # Find function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # compress path
            return parent[x]

        # Union function with union by rank
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False  # They are already connected — cycle detected!

            # Merge smaller tree into larger one
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

            return True  # Union successful

        # Process each edge
        for u, v in edges:
            if not union(u, v):  # If union fails (cycle), this is the redundant edge
                return [u, v]
