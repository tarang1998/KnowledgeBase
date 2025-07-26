from typing import List

class Solution:
    # Time Complexity : O(n*m)
    # space Complexity : O(n*m) 
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get number of rows (m) and columns (n)
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0

        # Track the maximum island area found
        max_area = 0

        # Helper function: DFS to compute area of island starting at (x, y)
        def dfs(x: int, y: int) -> int:
            # If out of bounds or water (0), this cell contributes 0 area
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                return 0
            # Mark this cell as visited by setting it to 0
            grid[x][y] = 0
            # 1 for this cell + explore all 4 directions
            return (1 + dfs(x+1, y)
                      + dfs(x-1, y)
                      + dfs(x, y+1)
                      + dfs(x, y-1))

        # Iterate over every cell in the grid
        for i in range(m):
            for j in range(n):
                # If we found an unvisited land cell (1), start a DFS
                if grid[i][j] == 1:
                    # Get the full island's area
                    area = dfs(i, j)
                    # Update max_area if this island is larger
                    if area > max_area:
                        max_area = area

        return max_area
