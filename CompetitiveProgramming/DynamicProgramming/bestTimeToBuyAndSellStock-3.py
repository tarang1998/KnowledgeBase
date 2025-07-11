class Solution:
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)  # Number of days (length of price list)
        dp = {}  # Dictionary to store already computed results for subproblems

        # Recursive function that computes the max profit
        # index     = current day
        # isBuying  = True if we can buy on this day, False if we need to sell
        # cap       = how many transactions we have left (max is 2)
        def dfs(index, isBuying, cap):
            # Base Case 1: If we’ve passed the last day, no profit can be made
            if index > n - 1:
                return 0

            # Base Case 2: If we've used up our 2 transactions, we can't trade anymore
            if cap == 0:
                return 0

            # If we've already computed this state before, return the cached result
            if (index, isBuying, cap) in dp:
                return dp[(index, isBuying, cap)]

            # If we are allowed to buy on this day
            if isBuying:
                # Option 1: Buy the stock today, so we spend money (subtract price), and move to sell mode
                buy = dfs(index + 1, False, cap) - prices[index]

                # Option 2: Skip buying today (cooldown), stay in buying mode
                cooldown = dfs(index + 1, True, cap)

                # We take the max of the two options to maximize profit
                dp[(index, isBuying, cap)] = max(buy, cooldown)
                return dp[(index, isBuying, cap)]

            else:
                # We are in sell mode (we already bought before)

                # Option 1: Sell the stock today, so we earn money (add price)
                # After selling, we reduce cap (used one transaction) and go back to buy mode
                sell = dfs(index + 1, True, cap - 1) + prices[index]

                # Option 2: Skip selling today (cooldown), stay in sell mode
                cooldown = dfs(index + 1, False, cap)

                # Take the max of selling or skipping
                dp[(index, isBuying, cap)] = max(sell, cooldown)
                return dp[(index, isBuying, cap)]

        # We start from day 0, with buying allowed, and 2 transactions available
        return dfs(0, True, 2)
