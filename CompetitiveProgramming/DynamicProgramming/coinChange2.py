class Solution:

    # Memory Efficient bottum up approach
    # Time Complexity : O(amount * no of coins)
    # Space Complexity : O(amount)
    def change(self,amount: int, coins: List[int]) -> int:

        dp = [0] * (amount+1)

        dp[0] = 1

        for i in range(len(coins)-1,-1,-1):
            newdp = [0] * (amount+1)
            newdp[0] = 1

            for j in range(1,amount+1):

                # The no of combination to get amount denoted by j considering the previous set of coins (without considering i)
                newdp[j] = dp[j]

                # After subtracting the coin i from the amount j if the value is greater than zero
                # Add no of combinations that can be obtained from amount (j - coins[i]) using the same set of coins
                if(j - coins[i] >= 0 ):
                    newdp[j] += newdp[j - coins[i]]
            
            dp = newdp
        return dp[amount]





    # Using 2-D array bottum up approach
    # Time Complexity : O(amount * no of coins)
    # Space Complexity : O(amount * no of coins)
    def change2(self,amount:int,coins:List[int]) -> int:
        
        # mem table
        # amount + 1 : no of rows 
        # len(coins) + 1 ; no of columns
        dp = []

        for i in range(amount+1):
            t = []
            for j in range(len(coins)+1):
                if(i == 0):
                    # Assigning value : 1 for all the coins when the amount is 0 
                    t.append(1)
                else:
                    t.append(0)
            dp.append(t)

        
        for i in range(1,amount+1):
            for j in range(len(coins)-1,-1,-1):

                # dp[i][j] shows the no of combinations to obtain amount i from coins[j:]
                # First assigning dp[i][j] to dp[i][j+1] : The no of combinations to obtain amount i from coins[j+1:]
                dp[i][j] = dp[i][j+1]

                # After subtracting the coin denoted by index j from the amount i if the result is greater than 0
                # Add dp[i-coins[j]][j] : The no of combinations to obtain amount i-coins[j] from coins[j+1:]
                if(i - coins[j] >= 0):
                    dp[i][j] += dp[i-coins[j]][j]

        return dp[amount][0]
         
    # Recursive Soltion
    # Time Complexity : O(amount * no of coins)
    # In order to avoid all the duplicate combinations 
    # Consider amount = 5 coins = [1,2,5]
    # Suppose we have chosen 1 initially we can use coins -> 1,2,5
    # When we choose 2 in the next iteration we can work with only -> 2,5
    def change1(self, amount: int, coins: List[int]) -> int:

        # key : (index,amountleft)
        # value : no of combinations possible
        dp = {}

        # index acts as a pointer to which coins we can use 
        # total amount : amount left 
        def dfs(index,totalAmount):


            if(index == len(coins)):
                return 0

            if(totalAmount < 0 ):
                return 0

            if(totalAmount == 0):
                return 1

            if((index,totalAmount) in dp):
                return dp[(index,totalAmount)]

            
            dp[(index,totalAmount)] = dfs(index,totalAmount - coins[index]) + dfs(index+1,totalAmount)

            return dp[(index,totalAmount)]


        return dfs(0,amount)