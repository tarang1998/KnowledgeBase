from collections import deque
from typing import List

class Solution:
    # Time Complexity : O(n*m)
    # Space Complexity : O(n*m)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get grid dimensions
        rows = len(grid)
        cols = len(grid[0]) if rows else 0

        queue = deque()
        fresh_count = 0

        # Step 1: Initialize by adding all initially rotten oranges to the queue
        # and counting fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # If there's no fresh oranges, return 0 immediately
        if fresh_count == 0:
            return 0

        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 2: BFS per minute – process all currently rotten oranges
        while queue and fresh_count > 0:
            minutes += 1  # A minute passes
            for _ in range(len(queue)):
                x, y = queue.popleft()
                # Check all four neighbors
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # If neighbor is in bounds and is a fresh orange
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2           # It turns rotten
                        fresh_count -= 1           # Decrease fresh count
                        queue.append((nx, ny))     # Enqueue for next minute

        # Step 3: After BFS, check if any fresh orange remains
        return minutes if fresh_count == 0 else -1
