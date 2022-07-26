class Solution:
    
    def findElementLinearComplexity(self,nums):
        
        ans = 0
        
        for i in range(len(nums)):
            
            ans = nums[i] ^ ans 
            
        return ans
    
    
    
    def findElementLogarithmicComplexity(self,nums):
        
        low = 0 
        
        high = len(nums)-1
        
        while(low<high):
            
            
            mid = (low+high)//2
            

            
            if(mid % 2 == 0 ):
                
                #the mid is on the right side
                if(nums[mid] == nums[mid-1]):
                    high = mid-2
                    
                #the mid is on the left side
                elif(nums[mid] == nums[mid+1]):
                    low = mid + 2
                    
                else:
                    return nums[mid]
                
            else:
                
                #the mid is on the right side
                if(nums[mid] == nums[mid+1]):
                    high = mid - 1
                    
                #the mid is on the left side
                elif(nums[mid] == nums[mid-1]):
                    low = mid + 1
                    
                else:
                    return nums[mid]
            
        return nums[low]
                    
                
        
        
        
            
            
    
    def singleNonDuplicate(self, nums):
        
        #return self.findElementLinearComplexity(nums)
        
        return self.findElementLogarithmicComplexity(nums)
        
        
        

        
        
        
        