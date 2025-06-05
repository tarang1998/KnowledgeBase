class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int: 

        dp = [amount + 1] * (amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            currAmount = i 
            for coin in coins:
                if currAmount - coin >= 0:
                    dp[i] = min(dp[i],1+dp[currAmount-coin])
        
        return dp[amount] if dp[amount]!= amount+1 else -1 

 
    
    def coinChange1(self, coins: List[int], amount: int) -> int: 
        mem = {}
        def recurse(amount):
            if amount < 0:
                return -1 
            if amount == 0:
                return 0 
            if amount in mem:
                return mem[amount]
            minVal = -1 
            for coin in coins:
                res = recurse(amount - coin)
                if res != -1:
                    if minVal == -1:
                        minVal = 1 + res
                    else:
                        minVal = min(minVal,1 + res)
            mem[(amount)] = minVal
            return minVal
        return recurse(amount)
        