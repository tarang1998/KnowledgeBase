class Solution:
    
    # Time Complexity : O(m+n)
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False
    
        wordCount = {}
        
        for i in range(len(s)):
            
            if(s[i] not in wordCount):
                
                wordCount[s[i]] = 1
                
            else:
                wordCount[s[i]] +=1
                
        for j in range(len(t)):
            
            if(t[j] not in wordCount):
                
                return False
            
            else:
                
                if(wordCount[t[j]] == 0):
                    return False
                
                wordCount[t[j]] -= 1
                
        return True
            
            
            
            
                
        