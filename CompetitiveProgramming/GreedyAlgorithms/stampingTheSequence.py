#https://leetcode.com/problems/stamping-the-sequence/

class Solution:
    
    def equals(self,target,stamp,position):
        
        for j,c in enumerate(stamp):
            if not (target[position + j] == c or target[position + j] == '?'):
                return False
        return True
    
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        target = [c for c in target]
        
        N = len(target)
        
        M = len(stamp)
        
        result = []
        
        parsed = []
        
        for i in range(N-M+1):
            #print(i)
            if self.equals(target,stamp,i):
                for j in range(i,-1,-1):
                    #print(i,j)
                    if j in parsed:
                        break
                    parsed.append(j)
                    if self.equals(target,stamp,j):
                        result.append(j)
                        target[j:j+M] = ['?'] * M
                    #print(parsed, result, target)
        return result[::-1] if all([c == '?' for c in target]) else []
        
         
        
        
        
        
        
        