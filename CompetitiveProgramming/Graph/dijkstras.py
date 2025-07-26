# Algorithm to find the shortest path from the source to all other vertices in a graph
# Dijkstras algorithm can be used for directed and undirected graphs 
# Cant be used on graphs with negative weight cycles (any negative edge)



import heapq  # Python library for heap operations (priority queue)

class Solution:
    # Time Complexity is O((V + E) log V) where V is the number of vertices and E is the number of edges
    # Space Complexity is O(V) for the distance array and O(V + E) for the adjacency list
    def dijkstra(self, V, edges, src):
        # Step 1: Build adjacency list from edge list
        # adj[u] = [(neighbor, weight), ...]
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # because graph is undirected
    
        # Step 2: Initialize distances array with "infinity"
        dist = [float('inf')] * V
        dist[src] = 0  # Distance to source is 0
    
        # Step 3: Min-heap to pick the node with smallest distance so far
        min_heap = [(0, src)]  # (distance, node)
    
        # Step 4: While there are nodes to process
        while min_heap:
            d_u, u = heapq.heappop(min_heap)
            # If we've already found a better path before, skip
            if d_u > dist[u]:
                continue
    
            # Step 5: Explore all neighbors of current node
            for v, weight in adj[u]:
                new_dist = d_u + weight
                # If going via u gives a shorter path to v, update it
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(min_heap, (new_dist, v))
    
        # Step 6: Return distances array
        return dist
            