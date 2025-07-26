from typing import List

class Solution:
    # Time Complexity : O(n*m)
    # Space Complexity : O(n*m)
    def solve(self, board: List[List[str]]) -> None:
        """
        Modify the board in-place: Flip all 'O's fully surrounded by 'X' into 'X',
        but leave 'O's connected to the border (not fully surrounded).
        """

        # Edge case: empty board
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(r: int, c: int):
            # If out of bounds or not an 'O', stop the DFS
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            # Temporarily mark safe 'O' to avoid flipping later
            board[r][c] = '#'
            # Explore all four directions
            dfs(r-1, c)  # up
            dfs(r+1, c)  # down
            dfs(r, c-1)  # left
            dfs(r, c+1)  # right

        # 1. Mark all 'O's connected to the border as safe ('#')
        # Top and bottom rows
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m-1][j] == 'O':
                dfs(m-1, j)
        # Left and right columns
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)

        # 2. Flip all remaining 'O' (surrounded) to 'X', and restore '#' to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # Flip surrounded 'O'
                elif board[i][j] == '#':
                    board[i][j] = 'O'  # Restore safe 'O'
