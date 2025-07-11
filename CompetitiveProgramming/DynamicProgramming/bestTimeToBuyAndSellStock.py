class Solution:
    
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def maxProfit(self, prices):
        # Initialize the minimum price so far to a very large number (infinity)
        # This will help us keep track of the lowest price we've seen as we loop through the list
        min_price = float('inf')  # infinity acts like the biggest possible number

        # Initialize max_profit to 0 because initially we haven't made any transaction
        max_profit = 0

        # Loop through each price in the list one by one
        for price in prices:
            # If the current price is lower than the minimum price we've seen so far,
            # we update min_price to be this lower price
            if price < min_price:
                min_price = price  # This becomes the new lowest buying price
            else:
                # Otherwise, we calculate the profit if we bought at min_price and sold at current price
                profit = price - min_price  # Selling price - Buying price

                # If this profit is greater than the maximum profit we've seen so far,
                # then we update max_profit to this new value
                if profit > max_profit:
                    max_profit = profit

        # After the loop, max_profit holds the best possible profit we could have made
        return max_profit
            
        