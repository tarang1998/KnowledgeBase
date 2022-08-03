class Solution:
    
    visited = None
    
    
    
    def parseGraph(self,row,column,grid):
        
       
        
        if(row<0 or row>len(grid)-1):
            return
        
        if(column<0 or column>len(grid[0])-1):
            return
        
        if(grid[row][column] == "0"):
            return
        
        if(self.visited[row][column] == 1):
            return
        

        
        self.visited[row][column] = 1
        
        
        self.parseGraph(row-1,column,grid)
        
        self.parseGraph(row,column-1,grid)
        
        self.parseGraph(row,column+1,grid)
        
        self.parseGraph(row+1,column,grid)
        
        
            
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.visited = []
        
        islandCount = 0 
        
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[i])):
                row.append(0)
            self.visited.append(row)
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if( grid[i][j] == "1" and self.visited[i][j] == 0):
                  
                    islandCount += 1
                    self.parseGraph(i,j,grid)
                    
        return islandCount
            
        
        
        
        
        
        
        