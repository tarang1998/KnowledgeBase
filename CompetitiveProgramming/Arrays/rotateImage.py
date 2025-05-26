class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        def transpose(matrix):
            for i in range(rows):
                for j in range(i,cols):
                    temp = matrix[j][i]
                    matrix[j][i] = matrix[i][j]
                    matrix[i][j] = temp

        def reflect(matrix):
            for i in range(rows):
                for j in range(cols//2):
                    temp = matrix[i][cols-1-j]
                    matrix[i][cols-1-j] = matrix[i][j]
                    matrix[i][j] = temp 



        transpose(matrix)
        reflect(matrix)



