class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        # The user can be in one of the three states :
        # Buying, Selling, Cooldown

        # Buying Status : True
        # Selling Status : False

        # key : (index, isBuying boolean status)
        # value : Profit obtained
        dp = {}



        def dfs(index, isBuying):

            if(index >= len(prices)):
                return 0

            if (index,isBuying) in dp:
                return dp[(index,isBuying)]

            #Check the state the user is in currently
            #If he is in the state where he has to buy a stock
            if(isBuying):

                #The user has two options 
                #Either buy the stock 
                #Or dont do anything -> cooldown

                #If the user buys the stock subtract by the cost of the stock
                buy = dfs(index+1, not isBuying) - prices[index]
                cooldown = dfs(index+1 , isBuying)
                dp[(index,isBuying)] = max(buy,cooldown)
                return dp[(index,isBuying)]

            #If the user is in the state where he has to sell the stock
            else:

                #The user has two options 
                #The user sells the stock
                #The user doesnt do anything 

                #If the user has sold the stock add the price of the stock
                sell = dfs(index+2, not isBuying) + prices[index]
                cooldown = dfs(index+1, isBuying)
                dp[(index,isBuying)] = max(sell,cooldown)
                return dp[(index,isBuying)]

        return dfs(0,True)









        
        