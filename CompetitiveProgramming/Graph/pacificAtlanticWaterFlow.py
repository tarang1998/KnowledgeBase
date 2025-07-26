
from collections import deque
from typing import List

class Solution:
    # Time Complexity : O(n*m)
    # Space Complexity : O(n*m)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Grid dimensions
        m = len(heights)
        n = len(heights[0]) if m > 0 else 0

        # Sets to track cells that can reach each ocean
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        # Directions for visiting neighbors (up, down, left, right)
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        # BFS starting from the ocean borders
        def bfs(starts, visited):
            q = deque(starts)
            while q:
                x, y = q.popleft()
                visited[x][y] = True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    # If neighbor is inside bounds, not visited, and higher or equal height
                    if (0 <= nx < m and 0 <= ny < n and
                        not visited[nx][ny] and
                        heights[nx][ny] >= heights[x][y]):
                        visited[nx][ny] = True
                        q.append((nx, ny))

        # Initialize BFS starting positions for Pacific (top row & left column)
        pac_starts = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
        bfs(pac_starts, pacific)

        # Initialize BFS for Atlantic (bottom row & right column)
        atl_starts = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]
        bfs(atl_starts, atlantic)

        # Collect cells reachable by both oceans
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])

        return result
