#https://practice.geeksforgeeks.org/problems/topological-sort/1

class Solution:
    
    #Function to return list containing vertices in Topological order.
    
    visited = {}
    
    stack = []
                
  
    def topoSort(self, V, adj):
        
        indegree = {}
        
        stack = []
        
        topo = []
         
        for vertex in range(V):
            
            if vertex not in indegree:
                    indegree[vertex] = 0
            
            for adjVertex in adj[vertex]:
            
                if adjVertex in indegree:
                    indegree[adjVertex] += 1
                else:
                    indegree[adjVertex] = 1
                    

      
        
        for vertex,indegreeCount in indegree.items():
        
            if(indegreeCount == 0 ):
                
                stack.append(vertex)
                
        while(len(stack) != 0 ):
            
            firstvertex = stack.pop(0)
            topo.append(firstvertex)

            
            adjNodes = adj[firstvertex]
            
            for adjNode in adjNodes:
                indegree[adjNode] -= 1
                if(indegree[adjNode] == 0 ):
                    stack.append(adjNode)
                    
        return topo



#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)

# } Driver Code Ends