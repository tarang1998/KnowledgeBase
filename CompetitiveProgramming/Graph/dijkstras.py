class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    
    def findVertexWithMinDistanceFromSource(self,spt,distance):
        
        minDistance = float('inf')
        vertex = None
        
        for i in range(len(distance)):
            if((i not in spt) and (distance[i] < minDistance)):
                minDistance = distance[i]
                vertex = i
                    
        return vertex
                
    
    def dijkstra(self, V, adj, S):
        
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


#{ 
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