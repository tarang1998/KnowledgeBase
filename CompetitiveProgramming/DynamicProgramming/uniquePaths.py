class Solution:

    # Time Complexity : O(n*m)
    # Space Comlexity : O(n)
    def uniquePaths(self, m: int, n: int) -> int:

        # Each element in the last row would have only one way to reach the finish point
        row = [1] * n

        for i in range(m-2,-1,-1):

            # Computing unique paths for the row above
            temp = [1] * n

            for j in range(n-2,-1,-1):
                temp[j] = temp[j+1] + row[j]

            row = temp

        return row[0]


    def uniquePaths2(self, m: int, n: int) -> int:

        mem = {}

        def traverse(m,n):

            if (m,n) in mem:
                return mem[(m,n)]

            if m == 1 and n == 1:
                return 1 

            if m < 1:
                return 0 
            
            if n < 1:
                return 0

            mem[(m,n)] =  traverse(m-1,n) + traverse(m,n-1)
            return mem[(m,n)]

        return traverse(m,n)

        