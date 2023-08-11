class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if(len(matrix) == 0):
            return False

        rowCount = len(matrix)

        columnCount = len(matrix[0])



        #Select the target row

        low = 0 

        high = rowCount - 1


        while low <= high:

            mid = (low + high)//2

            if(matrix[mid][0] == target):

                return True

            if(matrix[mid][0] > target):

                high = mid - 1
            
            else:

                low = mid + 1

        if(high < 0):
            return False 

        targetRow = high


        #Search for the target in the target row 

        left = 0

        right = columnCount-1


        while left <= right :

            mid = (left + right)//2

            if(matrix[targetRow][mid] == target):

                return True
            
            if(matrix[targetRow][mid] > target):

                right = mid - 1
            
            else:

                left = mid + 1

            
        return False






            


    def searchMatrixBruteForce(self, matrix: List[List[int]], target: int) -> bool:

        result = False

        for l in matrix :

            if target in l:

                return True

            if  target < l[-1]:

                return False

        return result

