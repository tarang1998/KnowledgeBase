class Solution:
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        #key : letter in a word 
        #value : positions at which the particular letter has occured
        
        wordPattern = {}
        
        
        for i in range(len(pattern)):
            
            currEle = pattern[i]
            
            if(currEle in wordPattern):
                wordPattern[currEle].append(i)
                
            else:
                wordPattern[currEle] = [i]
        
                
        solution =  []
       
    
        wordPatternValues = list(wordPattern.values())
        
        
                
        for i in range(len(words)):
            
            word = words[i]
            
            if(len(word) != len(pattern)):
                continue
              
            temp = {}
            isWordValid = True
               
            for j in range(len(word)):
                letter = word[j]

               
                if(letter in temp):
                    keys = list(temp.keys())
                    index = keys.index(letter)
                    if(j not in wordPatternValues[index]):
                        isWordValid = False
                        break
                    temp[letter].append(j)
                else:
                    temp[letter]=[j]
                    index = len(temp)-1
                    if(len(temp) > len(wordPatternValues)  or (j not in wordPatternValues[index])):
                        isWordValid = False
                        break
                        
            if(not isWordValid):
                continue
               
            if(list(temp.values()) == wordPatternValues ):
                solution.append(word)
               
        
        return solution       
                    
                    
                
               
              
               
              
            
            
                
                
            
            
            
            
            
        
        