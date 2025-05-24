class Solution:

    # Time Complexity : O(n*m)
    # Space Complexity : O(m)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # Calculate the number of possible paths for the last row elements 

        rowPath = [0] * cols

        for c in range(cols-1,-1,-1): 
            if obstacleGrid[rows-1][c] == 0:
                rowPath[c] = 1 
            else:
                break

        for r in range(rows-2,-1,-1):

            temp = [0] * cols

            for i in range(cols-1,-1,-1):

                if obstacleGrid[r][i] == 0:
                    temp[i] = rowPath[i]
                    if i < cols -1:
                        temp[i] += temp[i+1]

            rowPath = temp

        return rowPath[0]



        
        