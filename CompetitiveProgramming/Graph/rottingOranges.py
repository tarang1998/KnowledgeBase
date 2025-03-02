class Solution:

    # Time Complexity : O(n * m)
    # Space Complexity : O(n *m)
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        time = 0  
        rottenOranges = deque()
        freshOranges = 0 

        # Identify the rotten oranges and no of fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rottenOranges.append((r,c))
                if grid[r][c] == 1:
                    freshOranges += 1 
        

        # Perform bfs
        while rottenOranges and freshOranges:
            length = len(rottenOranges)
            for i in range(length):
                r,c = rottenOranges.popleft()
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr<0 or nr>=ROWS or nc<0 or nc>=COLS or grid[nr][nc] == 0 or grid[nr][nc] == 2):
                        continue
                    rottenOranges.append((nr,nc))
                    grid[nr][nc] = 2 
                    freshOranges -= 1
            time += 1

        return time if not freshOranges else -1






        