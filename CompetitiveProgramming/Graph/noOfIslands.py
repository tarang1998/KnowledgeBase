from typing import List

class Solution:
    # Time Complexity : O(n*m)
    # space Complexity : O(n*m) 
    def numIslands(self, grid: List[List[str]]) -> int:
        # Number of rows (m) and columns (n)
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0

        # Count of islands found
        island_count = 0

        # DFS helper function to mark all connected land as visited
        def dfs(x: int, y: int):
            # Check boundary conditions and only proceed if cell is land ('1')
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != '1':
                return
            # Mark this cell as visited by changing '1' to '0'
            grid[x][y] = '0'

            # Recursively explore four directions: up, down, left, right
            dfs(x - 1, y)  # up
            dfs(x + 1, y)  # down
            dfs(x, y - 1)  # left
            dfs(x, y + 1)  # right

        # Iterate through every cell in the grid
        for i in range(m):
            for j in range(n):
                # If we find unvisited land ('1'), we found a new island
                if grid[i][j] == '1':
                    island_count += 1  # Increment island counter
                    dfs(i, j)           # Use DFS to mark the whole island

        return island_count
