class Solution:

    
    def uniquePaths(self, m: int, n: int) -> int:

        #All the elements in the last row would have one way to reach the destination
        row = [1] * n

        #Loop through m-1 rows from bottom up 
        for i in range(m-1):

            temp = [1] * n

            # The last element of each row would also have only one way to reach to the destination
            for j in range(n-2,-1,-1):

                # The no of paths to reach the destination is equal to the
                # no of paths from the right element + no of paths from the bottom element
                temp[j] = temp[j+1] + row[j]

            row = temp

        # Returns the number of unique paths required to traverse from grid[0][0] to grid[m-1][n-1]
        return row[0]



        
      
        
        
        