# https://leetcode.com/problems/ransom-note/

from collections import Counter

class Solution:
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        
        magazineWordCount = {}
        
        for letter in magazine:
            
            if letter not in magazineWordCount:
                magazineWordCount[letter] = 1
                
            else:
                magazineWordCount[letter] += 1
                
        for letter in ransomNote:
            
            if (letter not in magazineWordCount or magazineWordCount[letter] == 0):
                return False
            
            magazineWordCount[letter] -= 1
            
        return True 
        
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        rn = Counter(ransomNote)
        mg = Counter(magazine)
        
        for k,v in rn.items():
            
            if k not in mg or mg[k] < v:
                return False
        return True