class Solution:
    
    solution  = []
    
    def findPermutations(self,nums,l,r):
        
        if (l == r ):
            
            self.solution.append(nums.copy())
            
        for i in range(l,r+1):
            
            nums[l], nums[i] = nums[i],nums[l]
            self.findPermutations(nums,l+1,r)
            nums[l], nums[i] = nums[i],nums[l]

            
            
        
        
        

    def permute(self, nums):
        
        self.solution = []
        
        self.findPermutations(nums,0,len(nums)-1)
        
        return self.solution;
    
    
        
        
        
        