
class Solution:
    # Time complexity : O(n) : Each state is defined by (index, isBuying) → 2 choices per day × n days = 2n states.
    # Space Complexity : O(n)
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)  # total number of days
        dp = {}  # dictionary to memoize (store) the result of subproblems

        # Define a recursive function that returns the max profit starting from a given day
        # 'index' tells which day we're at
        # 'isBuying' tells if we are allowed to buy on this day (True) or must sell (False)
        def dfs(index, isBuying):
            # Base case: if index goes beyond the last day, we can't make any profit
            if index > n - 1:
                return 0

            # If we've already computed the result for this (index, isBuying) pair, return it
            if (index, isBuying) in dp:
                return dp[(index, isBuying)]

            # If we are allowed to buy on this day
            if isBuying:
                # Option 1: Buy today, so we subtract today's price and change state to "not allowed to buy"
                buy = dfs(index + 1, False) - prices[index]

                # Option 2: Skip (cooldown), stay in the "buying" state and move to the next day
                cooldown = dfs(index + 1, True)

                # Store the best of the two options
                dp[(index, isBuying)] = max(buy, cooldown)
                return dp[(index, isBuying)]

            else:
                # If we are in "selling" mode (we already bought earlier)

                # Option 1: Sell today. Add today's price to profit and skip one day (cooldown)
                sell = dfs(index + 2, True) + prices[index]

                # Option 2: Skip selling today (just cooldown without selling), stay in "not allowed to buy"
                cooldown = dfs(index + 1, False)

                # Store the best of the two options
                dp[(index, isBuying)] = max(sell, cooldown)
                return dp[(index, isBuying)]

        # Start recursion from day 0, and we're initially allowed to buy
        return dfs(0, True)
