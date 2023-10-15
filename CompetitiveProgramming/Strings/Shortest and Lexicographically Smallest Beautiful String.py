class Solution:   
    
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        
        slbs = ""
        
        def checklex(s1,s2):
            
            for i in range(len(s1)):
                
                if(s1[i] > s2[i]):
                    return s2
                elif(s2[i] > s1[i]):
                    return s1
                
            return s1
                    
        
        for i in range(len(s)):
            
            k_count = 0 

            for j in range(i,len(s)): 
                
                if s[j] == "1":
                    
                    k_count +=1
                    
                if(k_count == k):
                    if(len(slbs) == len(s[i:j+1])):
                        slbs = checklex(slbs,s[i:j+1])
                    if(len(slbs) > len(s[i:j+1])):
                        slbs = s[i:j+1]
                    if(slbs == ""):
                        slbs = s[i:j+1]
                    break
                        
        return slbs
                
                
                
                
    
        
        
        
        