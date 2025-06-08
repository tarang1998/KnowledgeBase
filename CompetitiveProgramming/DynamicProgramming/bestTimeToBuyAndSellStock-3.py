class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        def dfs(index, isBuying, cap):
            if index > n-1:
                return 0 
            if cap == 0:
                return 0 
            if (index,isBuying,cap) in dp:
                return dp[(index,isBuying,cap)]
            if isBuying:
                buy = dfs(index+1, False,cap) - prices[index]
                cooldown = dfs(index+1, True, cap)
                dp[(index, isBuying, cap)] = max(buy,cooldown)
                return dp[(index, isBuying, cap)]
            else:
                sell =  dfs(index+1, True,cap-1) +  prices[index]
                cooldown = dfs(index+1, False, cap)
                dp[(index, isBuying, cap)] = max(sell,cooldown)
                return dp[(index, isBuying, cap)]
        return dfs(0,True,2)


        

        
   
        