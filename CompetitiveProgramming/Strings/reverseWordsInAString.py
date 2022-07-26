class Solution:
    
    def reverseWords(self, s):
        
        return " ".join(list(filter(lambda x : x != '',s.split(" ")))[::-1])
        
        
        
        
        
        
                
                
            
            
        