class Solution:

    mem = None
    
    def parse(self,coins,amount):

        if amount in self.mem:
            return self.mem[amount]

        minValue = float('inf')

        for coin in coins:

            if(amount - coin >= 0 ):
                
                minValue = min(minValue , 1 + self.parse(coins,amount-coin))

        self.mem[amount] = minValue
        print(amount,minValue)

        return self.mem[amount]


    
    def coinChange2(self, coins: List[int], amount: int) -> int:
        
        self.mem = {}

        self.mem[0] = 0

        self.parse(coins,amount)

        if(self.mem[amount] == float('inf')):
            return -1
        else:
            return self.mem[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}

        dp[0] = 0

        for t in range(1,amount+1):

            dp[t] = float('inf')

            for coin in coins:

                if(t - coin >= 0 ):

                    dp[t] = min(dp[t], 1+ dp[t-coin])

        
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]

                    












        