#https://practice.geeksforgeeks.org/problems/topological-sort/1

class Solution:
    
    visited = {}
    
    stack = []
    
    def parseGraph(self,node,adj):
        
        self.visited[node] = 1
        
        adjNodes = adj[node]
        
        for adjNode in adjNodes:
            
            if adjNode not in self.visited:
                
                self.parseGraph(adjNode,adj)
                
        self.stack.append(node)
        return 
        
                
        
        
        
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
    
        self.visited = {}
        
        self.stack = []
        

        for node in range(V):
            if(node not in self.visited):
                
                self.parseGraph(node,adj)
                
        self.stack.reverse()
        return self.stack
                
        
            
            



#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return Falsehttps://practice.geeksforgeeks.org/problems/topological-sort/1
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
    for i in range(t):https://practice.geeksforgeeks.org/problems/topological-sort/1
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