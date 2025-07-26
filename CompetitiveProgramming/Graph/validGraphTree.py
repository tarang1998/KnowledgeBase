from collections import defaultdict

class Solution:
    def validTree(self, n, edges):
        """
        Time Complexity: O(n + e) where n = number of nodes, e = number of edges
        Space Complexity: O(n + e) for graph and visited set
        """

        # Step 1: A tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False  # Not enough or too many edges to form a tree

        # Step 2: Build the undirected graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()  # Keeps track of visited nodes

        # Step 3: DFS to check for cycles
        def dfs(node, parent):
            visited.add(node)  # Mark current node as visited
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Don't go back to the parent
                if neighbor in visited:
                    return False  # Cycle detected
                if not dfs(neighbor, node):
                    return False
            return True  # All neighbors are okay

        # Start DFS from node 0
        if not dfs(0, -1):
            return False  # Cycle found

        # Step 4: After DFS, check if all nodes were visited (connected)
        return len(visited) == n  # True if connected, False if some nodes left out
