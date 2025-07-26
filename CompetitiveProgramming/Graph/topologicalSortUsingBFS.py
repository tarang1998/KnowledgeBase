
    
from collections import deque
from typing import List

class Solution:
    # Time Complexity : O(V + E) : We visit each vertex once and traverse each edge once
    # Space Complexity : O(V + E) : Storing adjacency lists and in-degree counts 

    def topoSort(self, V: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency list and compute in-degrees
        adj = [[] for _ in range(V)]
        indegree = [0] * V        # in-degree count for each node
        for u, v in edges:
            adj[u].append(v)      # edge u → v
            indegree[v] += 1      # v has one more incoming edge
    
        # Step 2: Initialize queue with all nodes having in-degree = 0
        queue = deque([i for i in range(V) if indegree[i] == 0])
        topo_order = []           # stores our topological ordering
    
        # Step 3: Process nodes with zero in-degree
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            # Decrease in-degree of all neighbors
            for nei in adj[node]:
                indegree[nei] -= 1
                # If a neighbor's in-degree becomes 0, it's ready to add
                if indegree[nei] == 0:
                    queue.append(nei)
    
        # Step 4: Check if graph had a cycle
        if len(topo_order) != V:
            # Not a DAG: cycle detected
            return []  # Or raise an error based on problem requirement
    
        return topo_order
