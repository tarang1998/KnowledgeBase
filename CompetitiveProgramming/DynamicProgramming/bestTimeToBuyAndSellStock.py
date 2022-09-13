class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        
        minValue = float('inf')
        maxProfit = 0 
        
        for price in prices:
            
            if price < minValue:
                minValue = price
                continue 
            
                
            if price - minValue > maxProfit:
                maxProfit = price - minValue
                
        return maxProfit
        
        