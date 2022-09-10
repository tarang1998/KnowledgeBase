class Solution:
    
    
    def partition(self,low,high,properties):
        
        swappingIndex = low-1
        
        aHigh = properties[high][0]
        bHigh = properties[high][1]
        
        for i in range(low,high):
            
            a = properties[i][0]
            b = properties[i][1]
            
            if(aHigh != a):
                if(a > aHigh):     
                    swappingIndex += 1
                    properties[swappingIndex],properties[i] = properties[i],properties[swappingIndex]
                          
            else:  
                if(b < bHigh):
                    swappingIndex += 1
                    properties[swappingIndex],properties[i] = properties[i],properties[swappingIndex]
                    
        swappingIndex += 1
        properties[high],properties[swappingIndex] = properties[swappingIndex],properties[high]
        
        return swappingIndex
                    
                
                
    
    def quickSort(self,low,high,properties):
        
        if(low > high):
            return
    
    
        p = self.partition(low,high,properties)
        
        self.quickSort(low,p-1,properties)
        
        self.quickSort(p+1,high,properties)
                
    
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        self.quickSort(0,len(properties)-1,properties)
                
        
        result = 0 
        
        maxValue = -float('inf')
        
        for i in range(len(properties)):
            
            
            if(maxValue > properties[i][1]):
                result += 1
            else:
                maxValue = properties[i][1]
                
        return result
       
                                
            
            
        
        
        