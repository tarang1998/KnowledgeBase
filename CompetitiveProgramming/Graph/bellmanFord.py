#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    adj: adjacency list for the graph
    S: Source
    '''
    
    def bellman_ford(self, V, adj, S):
        
        d = []
        
        for vertex in range(V):
            
            if(vertex == S):
                d.append(0)
            else:
                d.append(100000000)
                
                
        #Finding shortest distance from source to vertexes                
        for i in range(V):
            
            for u,v,w in adj:
                
                if d[u] != 100000000 and d[v] > d[u] + w:
                    d[v] = d[u] + w
                    
        
                
        #checking for negative cycle
        for u,v,w in adj:
            if(d[u] != 100000000  and d[v] > d[u] + w):
                print("Negative Cycle is present");
                return -1
            
            

        return d


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
        adj = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends