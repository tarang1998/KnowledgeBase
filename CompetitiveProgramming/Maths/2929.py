import math


class Solution:


    

    def distributeCandies(self, n: int, limit: int) -> int:


        def comb(n, k):
            """
            Helper function to compute n choose k.
            """
            if n < 0 or k < 0 or k > n:
                return 0
            return math.comb(n, k)  # Using built-in combinatorics

        """
        Counts the number of valid distributions of 'n' candies among 3 children
        such that no child gets more than 'limit' candies.
        """
        
        # Step 1. Count all solutions without limit (stars and bars)
        # n - candies (starts) and 3 - 1 = 2 (bars), to divide among 3 
        # Total positions : n + 3 - 1
        # No of selections : 3 - 1
        total_ways = comb(n + 2, 2)
        
        
        # Step 2. Subtract cases where at least one child exceeds the limit
        subtract_one_exceed = 0
        for i in range(3):
            # Give (limit+1) candies to one child and distribute the rest freely
            candies_left = n - (limit + 1)
            subtract_one_exceed += comb(candies_left + 2, 2)  # distribute to 3 kids
            # If candies_left < 0, comb() will return 0 automatically

        # Step 3. Add cases where at least two children exceed the limit
        add_two_exceed = 0
        for i in range(3):
            for j in range(i+1, 3):
                # Give (limit+1) candies to two kids and distribute the rest
                candies_left = n - 2*(limit + 1)
                add_two_exceed += comb(candies_left + 2, 2)
                # If candies_left < 0, comb() will return 0

        # Step 4. Subtract cases where all three children exceed the limit
        subtract_all_exceed = 0
        candies_left = n - 3*(limit + 1)
        subtract_all_exceed += comb(candies_left + 2, 2)
        # If candies_left < 0, comb() will return 0
        
        # Apply inclusion-exclusion
        valid_ways = total_ways - subtract_one_exceed + add_two_exceed - subtract_all_exceed
        
        return valid_ways




    def distributeCandies1(self, n: int, limit: int) -> int:


        count = 0 

        # Consider the children a x,y,z
        # Z can get candies ranging from 0 to min(n,limit)+1 

        for i in range(0,min(limit,n)+1):

            # max candies X+Y can have is 2*limit
            # n-i <= 2* limit
            if n-i<=2*limit:
                 

                # Find all possibilities for x

                # x+y == n-i 
                # y =  n-i-x
                # 0<=y<=limit

                # n-i-x>=0
                # n-i>=x

                # n-i-x <= limit
                # n-i-limit <=x

                # n-i-limit <= x <= n-i

                count += min(limit,n-i) - max(n-i-limit,0) + 1

        return count


    
            

            
        