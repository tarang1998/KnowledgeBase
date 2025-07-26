from typing import List
class Solution:
    # Time Complexity : O(V + E)
    # Space Complexity : O(V)
    
    def topoSortDFS(V: int, edges: List[List[int]]) -> List[int]:
        # Build adjacency list for the directed graph
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)

        visited = [False] * V       # To mark fully processed nodes
        temp_mark = [False] * V     # To detect cycles (if needed)
        stack = []                  # Holds nodes in reverse topological order

        def dfs(node: int):
            # Early stop if a cycle is detected (optional for DAGs)
            if temp_mark[node]:
                raise Exception("Cycle detected!")
            if visited[node]:
                return

            temp_mark[node] = True
            # Visit all neighbors first
            for nei in adj[node]:
                dfs(nei)
            temp_mark[node] = False

            visited[node] = True
            # Post-order: append after visiting all descendents
            stack.append(node)

        # Call DFS for every node
        for i in range(V):
            if not visited[i]:
                dfs(i)

        # Reverse the built stack to get correct topological order
        return stack[::-1]
