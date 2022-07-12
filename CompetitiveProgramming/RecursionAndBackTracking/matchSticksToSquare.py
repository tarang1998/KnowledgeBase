class Solution:
    
    
    def check(self,side1,side2,side3,side4,requiredSideLength,matchSticks,memo,index):
        
        if((side1,side2,side3,side4) in memo):
            return memo[(side1,side2,side3,side4)]
        
        if(side1 > requiredSideLength or side2 > requiredSideLength or side3 > requiredSideLength or side4 > requiredSideLength ):
            return False
        
        if(index == len(matchSticks)):
            return side1 == side2 == side3 == side4 == requiredSideLength
        
        ans = False
        
        
        ans = ans or self.check(side1 + matchSticks[index] ,side2,side3,side4,requiredSideLength,matchSticks,memo,index+1)
        ans = ans or self.check(side1 ,side2 + matchSticks[index],side3,side4,requiredSideLength,matchSticks,memo,index+1)  
        ans = ans or self.check(side1 ,side2,side3 + matchSticks[index],side4,requiredSideLength,matchSticks,memo,index+1)
        ans = ans or self.check(side1 ,side2,side3,side4 + matchSticks[index],requiredSideLength,matchSticks,memo,index+1)

        memo[(side1,side2,side3,side4)] = ans 
        
        return ans 
                
            
        
        
        
        
        
        
        
    def makesquare(self, matchsticks):
        
        memo = {}
        
        matchStickSum = sum(matchsticks)
        
        if(len(matchsticks) < 4):
            return False
        
        if(matchStickSum % 4 != 0):
            return False
        
        requiredSideLength = matchStickSum/4
        
        
        matchsticks.sort(reverse = True)
        
        return self.check(0,0,0,0,requiredSideLength,matchsticks,memo,0)
    
        
    
    
        
        
        
        
        
        
        