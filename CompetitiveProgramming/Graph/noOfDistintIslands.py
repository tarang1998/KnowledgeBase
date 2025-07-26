#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)

class Solution:
    # Time Complexity: O(m * n * log (m n))
    # Space Complexity: O(m * n)
    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)                # number of rows
        n = len(grid[0]) if m > 0 else 0  # number of columns
        unique_shapes = set()       # to store distinct island signatures

        # DFS that records all coordinates of the island
        def dfs(i: int, j: int, origin_i: int, origin_j: int, shape: List[tuple]):
            # boundary + visited + water check
            if (i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1):
                return
            grid[i][j] = 0  # mark visited
            # record relative position from the starting cell
            shape.append((i - origin_i, j - origin_j))

            # explore in all four directions
            dfs(i + 1, j, origin_i, origin_j, shape)
            dfs(i - 1, j, origin_i, origin_j, shape)
            dfs(i, j + 1, origin_i, origin_j, shape)
            dfs(i, j - 1, origin_i, origin_j, shape)

        # iterate every cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    shape = []
                    # discover entire island & record its shape
                    dfs(i, j, i, j, shape)
                    # normalize shape: sort and convert to tuple for set
                    unique_shapes.add(tuple(sorted(shape)))

        return len(unique_shapes)