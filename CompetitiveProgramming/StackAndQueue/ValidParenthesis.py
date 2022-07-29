class Solution:
    
    
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for i in range(len(s)):
            
            
            ele = s[i]
            
            
            if(ele == '(' or ele == '{' or ele == '['):
                
                stack.append(ele)
                
            elif(ele == ')'):
        
                
                if(len(stack) == 0 or stack[-1] != '('):  
                    return False
                else:
                    stack.pop()

                    
            elif(ele == '}'):
                
                if(len(stack) == 0 or stack[-1] != '{'):  
                    return False
                else:
                    stack.pop()
                    
            elif(ele == ']'):
                
               
                if(len(stack) == 0 or stack[-1] != '['):  
                    return False
                else:
                    stack.pop()
        
        if(len(stack) == 0 ):
            return True 
        else:
            return False
        
                    
            
            
        