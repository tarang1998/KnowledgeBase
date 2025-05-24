#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)

class Solution:

    # Time Complexity : O(n*m)
    # Space Complexity : O(n*m)
    def countDistinctIslands(self, grid : List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        
        visited = [[False] * cols  for _ in range(rows)]
        
        shapes = set()
        

        def dfs(r,c,base_r,base_c,path):
        
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
                
            if visited[r][c]:
                return 
                
            if grid[r][c] == 0:
                return 
            
            visited[r][c] = True
            
            path.append((r - base_r, c - base_c))  # save the relative position
            
            dfs(r+1, c, base_r, base_c, path)
            dfs(r-1, c, base_r, base_c, path)
            dfs(r, c+1, base_r, base_c, path)
            dfs(r, c-1, base_r, base_c, path)

        
        
        for i in range(rows):
            for j in range(cols):
                
                if not visited[i][j] and grid[i][j] == 1:
                    path = []
                    dfs(i,j,i,j,path)
                    shapes.add(tuple(path))
        
        return len(shapes)
                    
                
                    
                
                
                
                
                
            

            
                    
                    
                    
                    
            
            
            
            
            
            
            