class Solution:

    # Time Complexity : Log(n)
    # Space Complexity : O(1)
    def checkPowersOfThree(self, n: int) -> bool:

        # Convert the decimal into base 3
        # As we can use only distinct powers of 3 
        # If the digit 2 occurs in the base 3 representation of the decimal 
        # the result is false

        while n:
            if n%3 == 2:
                return False
            n = n//3
        
        return True 
        