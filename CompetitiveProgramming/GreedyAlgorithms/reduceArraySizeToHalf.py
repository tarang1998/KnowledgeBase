#https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    
    def minSetSize(self, arr: List[int]) -> int:
        
        N = len(arr)
        
        count = {}
        
        for ele in arr:
            
            if ele in count:
                count[ele] += 1
                
            else:
                count[ele] = 1
                
        sortedCount = sorted(count.items(),key = lambda x:x[1], reverse = True)
        
        result = 0 
        
        size = N
        
        for key,value in sortedCount:
            size -= value
            result += 1
        
            if(size <= N/2):
                break
                
        return result
            
            
                
        
            
            