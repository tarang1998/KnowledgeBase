#https://leetcode.com/problems/wiggle-subsequence/submissions/

import math

class Solution:
        
    
    def wiggleMaxLength(self, nums):
      
        
        down = 1
        up = 1
        
        for i in range(1,len(nums)):
            
            if(nums[i] - nums[i-1] > 0):
                
                up = down+1
                
            elif (nums[i] - nums[i-1] < 0):
                
                down = up+1
                
        return max(down,up)
        
        
        