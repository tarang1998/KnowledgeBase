

class Solution:
    
    # Time Complexity : O(n)
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        

        n = len(edges)

        node1Paths = [-1] * n
        node2Paths = [-1] * n

        def dfs(node,distance,distances):

            if distances[node] != -1:
                return

            if node == -1:
                return

            distances[node] = distance

            dfs(edges[node],distance+1,distances)

        dfs(node1,0,node1Paths)
        dfs(node2,0,node2Paths)

        result = n+1
        index = -1 

        for i in range(n):
            if node1Paths[i] != -1 and node2Paths[i] != -1:
                m = max(node1Paths[i], node2Paths[i])
                if (result > m):
                    result = m
                    index = i
        return -1 if index == -1 else index 

