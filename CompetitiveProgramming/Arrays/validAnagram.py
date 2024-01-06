class Solution:
    
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False

        mem = [0] * 26 

        for i in range(len(s)):
            mem[ord(s[i]) - ord('a')] += 1
            mem[ord(t[i]) - ord('a')] -= 1  
        
        return all(count == 0 for count in mem)


    
    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def isAnagram1(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False
    
        wordCount = {}
        
        # Fill the map with all characters of the first string
        for i in range(len(s)):
            
            if(s[i] not in wordCount):
                
                wordCount[s[i]] = 1
                
            else:
                wordCount[s[i]] +=1
        
        # Check if characters in the second string is present in the first string 
        for j in range(len(t)):
            
            if(t[j] not in wordCount):
                
                return False
            
            else:
                
                if(wordCount[t[j]] == 0):
                    return False
                
                wordCount[t[j]] -= 1
                
        return True
            
            
            
            
                
        