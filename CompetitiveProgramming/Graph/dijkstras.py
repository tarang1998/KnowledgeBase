# Dijkstras algorithm can be used for directed and undirected graphs 
# Cant be used on graphs with negative weight cycles

class Solution:

    #Dijkstras Agorithms using priority Queue
    # Time Complexity : O(ElogV)
    # Space Complexity : O(V)
    def dijkstra(self, V, adj, S):     

        # Create the min heap 
        pq = []
        hq.heapify(pq)
        
        # Initialize the distance of the nodes from the source
        dist = [float('inf')] * V
        dist[S] = 0 

        # Push the only known distance : (0,S)
        hq.heappush(pq,[0,S])
        
        while(pq):
            
            distance, node = hq.heappop(pq)

    
            for neighbour in adj[node]:
                
                neighbourDistance = neighbour[1]
                neighbourNode = neighbour[0]
                
                if(distance + neighbourDistance < dist[neighbourNode] ):
                    
                    dist[neighbourNode] = distance + neighbourDistance
                    hq.heappush(pq,[distance + neighbourDistance,neighbourNode])

        return dist

    
    
    def findVertexWithMinDistanceFromSource(self,spt,distance):
        
        minDistance = float('inf')
        vertex = None
        
        for i in range(len(distance)):
            if((i not in spt) and (distance[i] < minDistance)):
                minDistance = distance[i]
                vertex = i
                    
        return vertex
                
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    # Time Complexity : O(V^2)
    # Space Complexity : O(V)
    def dijkstra1(self, V, adj, S):
        
        # An array storing the shortest distance from the source 
        # Source vertex index is set to zero 
        # Rest vertices are set to infinity
        distanceFromSource = []
        
        for i in range(V):
            
            if (i == S):
                distanceFromSource.append(0)
            else:
                distanceFromSource.append(float('inf'))
           
        #Shortest path tree     
        spt = {}
        
        for count in range(V):
            
            vertex = self.findVertexWithMinDistanceFromSource(spt,distanceFromSource)
            spt[vertex] = 1
                
            adjNeighbours = adj[vertex]
            
            for adjNeighbour in adjNeighbours:
                
                v = adjNeighbour[0]
                weight = adjNeighbour[1]
                
                if(distanceFromSource[v] > distanceFromSource[vertex] + weight):
                
                    distanceFromSource[v] = distanceFromSource[vertex] + weight
                
                
        return distanceFromSource
                
            
                
                
                
            
        #code here

 
# Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends