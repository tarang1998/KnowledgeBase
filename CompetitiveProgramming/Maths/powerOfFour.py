#https://leetcode.com/problems/power-of-four/

import math

class Solution:
    
    def isPowerOfFour(self, n: int) -> bool:
        if(n > 0 and not(n & n-1) and int(sqrt(n))*int(sqrt(n)) == n and math.log(n,4).is_integer()):
            return True
        else:
            return False
        
        
        