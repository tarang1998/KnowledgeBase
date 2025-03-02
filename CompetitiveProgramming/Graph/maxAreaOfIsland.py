
# Time Complexity : O(n*m)
# Space Complexity : O(n*m)
class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [[-1,0],[0,1],[1,0],[0,-1]]

        maxArea = 0 

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0 

            area = 1

            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr<0 or nr>=ROWS or nc<0 or nc>=COLS or grid[nr][nc] == 0):
                        continue
                    grid[nr][nc] = 0 
                    area += 1
                    q.append((nr,nc))
            return area 
    

        def dfs(r,c):
            if(r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0 
            area = 1
            for dr,dc in directions:
                area += dfs(r+dr,c+dc)
            return area 


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    #area = dfs(r,c)
                    area = bfs(r,c)
                    if area > maxArea:
                        maxArea = area 

        return maxArea
        