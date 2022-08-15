#https://leetcode.com/problems/roman-to-integer/

class Solution:
    
    
    def romanToInt(self, s: str) -> int:
        
        totalValue = 0 
        
        romanValues = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        for i in range(len(s)):
            
            if( i != len(s)-1 ):
                
                value1 = romanValues[s[i]]
                value2 = romanValues[s[i+1]]
                
                if(value1 < value2):
                    totalValue -= value1
                else:
                    totalValue += value1
                
            else :
                
                totalValue += romanValues[s[i]]
                
        return totalValue
            
                
            
            
        