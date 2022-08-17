# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        alpMorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        startASCIIValue = 97
        
        alpMorseDict = {}
        
        for i in range(len(alpMorse)):
            
            alpMorseDict[chr(startASCIIValue+i)] = alpMorse[i]
            
            
        result = []
        
        for word in words:
            
            morseCode = ""
            for letter in word:
                morseCode += alpMorseDict[letter]
                
            result.append(morseCode)
            
        return len(set(result))
