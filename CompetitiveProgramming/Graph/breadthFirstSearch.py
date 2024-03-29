#https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

#User function Template for python3
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        
        bfs = []
        
        # Dictionary to keep record of all the nodes 
        # that have been visited previously
        visited = {}
        
        # FIFO Data Structure
        queue = [0]

        # Marking the root node as visited 
        visited[0]=1
        
        while(len(queue) != 0 ):
            
            ele = queue.pop(0)
            
            bfs.append(ele)
            
            # Visiting all the neighbours of the popped element 
            # marking then as visited 
            # and inserting them into the queue
            neighbors = adj[ele]
            
            for i in neighbors:
                if i not in visited:
                    visited[i] = 1
                    queue.append(i)
                    

            
        return bfs
            
            
            


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends