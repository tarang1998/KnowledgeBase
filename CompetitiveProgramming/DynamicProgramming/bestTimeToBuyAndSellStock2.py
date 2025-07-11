# You’re allowed to make as many transactions as you want — buy and sell multiple times — but you can only hold one stock at a time.
# So we just buy before the price goes up and sell when it’s higher than the previous day.

# This means:

# Anytime today's price > yesterday's price, we can consider this as profit.


class Solution:
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def maxProfit(self, prices):
        # Start with 0 profit because we haven't done any transactions yet
        total_profit = 0

        # Loop through the price list starting from the second day (index 1)
        for i in range(1, len(prices)):
            # Check if today's price is greater than yesterday's
            if prices[i] > prices[i - 1]:
                # If yes, then we could have bought yesterday and sold today
                # So we add the profit to our total profit
                profit = prices[i] - prices[i - 1]
                total_profit += profit  # Add that profit to total

        # After checking all days, return the total profit
        return total_profit
        
        