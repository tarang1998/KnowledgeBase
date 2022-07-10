import heapq

class Solution:
    
    
    def minCostClimbingStairs(self, cost):
        
        dp0 = cost[0]
        
        dp1 = cost[1]
        
        
        for i in range(2,len(cost)):
            
            cur = cost[i] + min(dp0,dp1)
            
            dp0 = dp1
            dp1 = cur
            
          
        return min(dp0,dp1)
            
            
        
        
        
        
        