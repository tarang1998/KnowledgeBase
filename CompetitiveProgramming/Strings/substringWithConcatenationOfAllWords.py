class Solution:
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        wordCount = len(words)
        
        wordLength = len(words[0])
        
        wordMap = {}
        
        for word in words:
            if(word not in wordMap):
                wordMap[word] = 1
            else:
                wordMap[word] += 1
        
        slidingWindow = [0,wordCount*wordLength]
        
        results = []
        
        while(slidingWindow[1] <= len(s)):
            
            
            startPos = slidingWindow[0]
            
            endPos = slidingWindow[1]
            
            pos = startPos
            windowWordMap = {}
            
            while(pos < endPos):
                
                word = s[pos:pos+wordLength]
                
                if (word in wordMap):
                    if(word not in windowWordMap):
                        windowWordMap[word] = 1
                        pos += wordLength
                    else:
                        if(windowWordMap[word] < wordMap[word]):
                            windowWordMap[word] += 1
                            pos += wordLength

                        else:
                            break
                        
                else:
                    break
                    
            if(windowWordMap == wordMap):
                results.append(startPos)
                
            slidingWindow[0] += 1
            slidingWindow[1] += 1
                
        return results
        
        
        