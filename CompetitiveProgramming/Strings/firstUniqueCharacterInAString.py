# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    
    def firstUniqChar(self, s: str) -> int:
        
        #saves tuple - first occurence position and count
        characterCount = {}
        
        for i in range(len(s)):
            
            if(s[i] in characterCount):
                characterCount[s[i]][1]+=1
            else :
                characterCount[s[i]] = [i,1]
                
        minIndex = None
        
        for key,value in characterCount.items():
            
            if(value[1] == 1 ):
                if(minIndex == None or minIndex > value[0]):
                    minIndex = value[0]
                
        if(minIndex == None):    
            return -1
    
        else:
            return minIndex 
            
        