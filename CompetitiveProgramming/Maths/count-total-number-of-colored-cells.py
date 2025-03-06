class Solution:

    # Time Complexity : O(1)
    # Space Complexity : O(1)
    def coloredCells(self, n: int) -> int:

        # At minute 1 , no of colored cell = 1

        # At minute 2
        # No of added cells = 4
        # Total Cells : 1 + 4 = 5 

        # At minute 3 
        # No of added cells = 8 
        # Total Cells : 8 + 5 = 13

        # At minute 4
        # No of added cells : 12 
        # Total cells : 12 + 13 = 25

        # The cells are added in a pattern : 4,8,12 
        # For n, the added cells would be according to : 4*(1+2+3+...+(n-1))
        # The total cells would be : 1 + 4*(1+2+3+...+(n-1)) =  1 + 4 * ((n * (n-1))//2)

        return 1 + 4 * ((n * (n-1))//2)
        
