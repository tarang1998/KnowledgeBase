class Solution:

    # Recursive Solution
    # Time Complexity : O(n*m)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        mem = {}

        def parse(i,j):
            if ((i,j) in mem):
                return mem[(i,j)]
            
            # Travesring in the upward direction
            up = 0 
            if(i > 0 and matrix[i-1][j]>matrix[i][j]):
                up = parse(i-1,j)

            # Traversing in the downward direction
            down = 0 
            if(i<len(matrix)-1 and matrix[i+1][j] > matrix[i][j]):
                down = parse(i+1,j)

            # Traversing in the left direction
            left = 0 
            if(j>0 and matrix[i][j-1] > matrix[i][j]):
                left = parse(i,j-1)

            # Traversing in the right direction
            right = 0 
            if(j < len(matrix[0])-1 and matrix[i][j+1] > matrix[i][j]):
                right = parse(i,j+1)

            t = 1 + max(up,down,left,right)

            mem[(i,j)] = t
            return t


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                parse(i,j)

        return max(mem.values())

        