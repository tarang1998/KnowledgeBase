class Solution:

    
    def uniquePaths(self, m: int, n: int) -> int:

        #All the elements in the last row would have one way to reach the destination
        row = [1] * n

        for i in range(m-1):

            temp = [1] * n

            for j in range(n-2,-1,-1):

                # The no of paths to reach the destination is equal to the
                # no of paths from the right element + no of paths from the bottom element
                temp[j] = temp[j+1] + row[j]

            row = temp

        return row[0]



        
      
        
        
        