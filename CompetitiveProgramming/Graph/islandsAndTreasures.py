from collections import deque
from typing import List

class Solution:
    # Time Complexity : O(n*m)
    # Space Complexity : O(n*m)
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Modify the grid in-place: for each land cell (INF), fill in the distance
        to its nearest treasure chest (0); water cells (-1) remain unchanged.
        """

        INF = 2**31 - 1
        m = len(grid)
        n = len(grid[0]) if m else 0

        # Multi-source BFS queue initialized with all treasures (value = 0)
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        # 4-directional moves
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        d = 0  # Current distance from treasure

        # BFS expansion from treasures outward
        while q:
            d += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    # Check boundary and that it's a land cell needing update
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == INF:
                        grid[nx][ny] = d       # Fill distance
                        q.append((nx, ny))     # Add for next expansion
