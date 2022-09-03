class Solution:
    

    def findSolutions(self,n,k,results,level,number):
        
        if(level == n ):
            results.append(int(number))
            return
            
        if(len(number) == 0 ):
            for i in range(1,10):
                self.findSolutions(n,k,results,level+1,number+str(i))
                
        else:
            prevDigit = int(number[len(number)-1])
            if(prevDigit + k < 10 ):
                self.findSolutions(n,k,results,level+1,number+str(prevDigit + k))
            if(prevDigit - k >= 0):
                self.findSolutions(n,k,results,level+1,number+str(prevDigit - k))

            
    
    
    
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        initialNo = ''    
        results = []

        
        self.findSolutions(n,k,results,0,initialNo)
        
        return list(set(results))
        
        
        