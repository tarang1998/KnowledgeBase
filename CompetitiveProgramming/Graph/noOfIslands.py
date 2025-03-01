# Using Depth First Search
# 1. Iterate through each element of the grid 
# 2. If the element is "1", perform DFS to recursively visit every 1 that is reachable (signifying a single island)
# 3. Mark the visited grid cell : "1" -> "0"
# 4. The no of groups of 1 correspond to the no of island 
# Time Complexity : O(n * m)
# Space Complexity : O(n * m)


# Using Breadth First Search
# 1. Iterate through each element of the grid 
# 2. If the cell is marked "1" perform BFS
# 3. Mark the visited grid cell : "1" -> "0"
# Time Complexity : O(n * m)
# Space Complexity : O(n * m)


class Solution:
    
    
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[1])

        islandCount = 0 

        directions = [[-1,0],[0,1],[1,0],[0,-1]]


        def dfs(r,c):
            if(r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0"
            for dr,dc in directions:
                dfs(r+dr,c+dc)


        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = "0"

            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r + dr,c + dc
                    if(nr<0 or nr>=ROWS or nc<0 or nc>=COLS or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"
                    
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c] == "1"):
                    islandCount += 1
                    dfs(r,c)
                            
        return islandCount
    


    
