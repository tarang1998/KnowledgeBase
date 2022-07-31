# https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

#User function Template for python3

class Solution:
    
    
   
    #Function to return a list containing the DFS traversal of the graph.
    
    def dfsOfGraph(self, V, adj):
        
        solution = []
        
        visited = {}
        
        
        
        def parseTree(vertex):
            
            visited[vertex] = 1 
            
            solution.append(vertex)
            
            edges  = adj[vertex]
            
            for i in edges:
                
                if(i in visited):
                    continue 
                
                parseTree(i)
                    
        
        
        
        
        
        parseTree(0)
        
        return solution
        

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends