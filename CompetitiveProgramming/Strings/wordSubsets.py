#https://leetcode.com/problems/word-subsets/

class Solution:
    
    
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        solution  = []
        
        words2Dict = {}

        for i in range(len(words2)):
            
            word = words2[i]
            
            temp = {}
                
            for j in word:
                
                if(j in temp):
                    temp[j] +=1
                else:
                    temp[j] = 1  
                    
            for k,v in temp.items():
                
                if(k not in words2Dict):
                    words2Dict[k] = v
                else:
                    if( v > words2Dict[k]):
                        words2Dict[k] = v
                    
            
        
        for i in range(len(words1)):
            
            temp = {}
            
            word = words1[i]
            
            
            for j in word:
                
                if(j in temp):
                    temp[j] += 1 
                else:
                    temp[j] = 1
            
            isUniversal = True 
        
                
            for k,v in words2Dict.items():
                    
                if((k not in temp) or temp[k] < v):
                    isUniversal = False
                    break
                    
            if(isUniversal):
                solution.append(word)
                
        return solution
            
                    
                
            
            
            
            
            
        
        